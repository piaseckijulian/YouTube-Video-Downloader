import { API_URL } from "$env/static/private"
import { formSchema } from "$lib/schema"
import type { ErrorResponse, VideoResponse } from "$lib/types"
import type { Config } from "@sveltejs/adapter-vercel"
import { fail } from "@sveltejs/kit"
import axios from "axios"
import { superValidate } from "sveltekit-superforms"
import { zod } from "sveltekit-superforms/adapters"
import type { Actions, PageServerLoad } from "./$types"

export const config: Config = {
  maxDuration: 60,
}

export const load: PageServerLoad = async () => {
  return {
    form: await superValidate(zod(formSchema)),
  }
}

export const actions = {
  default: async (event) => {
    const form = await superValidate(event, zod(formSchema))

    if (!form.valid) {
      return fail(400, {
        form,
      })
    }

    const videoUrl = form.data.videoUrl

    try {
      const { data } = await axios.get<VideoResponse>(
        `${API_URL}/download-video?url=${encodeURIComponent(videoUrl)}`,
      )

      const videoBase64 = data.videoBase64

      return {
        form,
        videoBase64,
        error: null,
      }
    } catch (error) {
      let errorMsg: ErrorResponse["detail"]

      if (axios.isAxiosError(error) && error.response?.data?.detail) {
        errorMsg = error.response.data.detail
      } else {
        errorMsg = "An unknown error ocurred"
      }

      console.error(errorMsg)

      return {
        form,
        videoBase64: null,
        error: errorMsg,
      }
    }
  },
} satisfies Actions
