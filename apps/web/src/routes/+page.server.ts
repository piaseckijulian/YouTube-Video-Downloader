import { formSchema } from '$lib/schema';
import type { ApiErrorRes } from '$lib/types';
import { fail } from '@sveltejs/kit';
import axios, { AxiosError } from 'axios';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  return {
    form: await superValidate(zod(formSchema))
  };
};

export const actions: Actions = {
  default: async event => {
    const form = await superValidate(event, zod(formSchema));

    if (!form.valid) {
      return fail(400, {
        form
      });
    }

    const videoUrl = form.data.videoUrl;
    const API_URL = process.env.API_URL as string;

    try {
      const { data } = await axios.get<ArrayBuffer>(
        `${API_URL}/downloadVideo?url=${encodeURIComponent(videoUrl)}`,
        { responseType: 'arraybuffer' }
      );

      const base64String = Buffer.from(data).toString('base64');

      return {
        form,
        videoBase64String: base64String,
        error: null
      };
    } catch (error) {
      if (error instanceof AxiosError) {
        const res = error.response?.data;
        const { error: errorMsg }: ApiErrorRes = JSON.parse(
          Buffer.from(res).toString()
        );

        console.error(errorMsg);

        return {
          form,
          videoBase64String: null,
          error: errorMsg
        };
      }
    }
  }
};
