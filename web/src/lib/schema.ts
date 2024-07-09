import { z } from "zod"

const YOUTUBE_VIDEO_REGEX = /^https:\/\/www\.youtube\.com\/watch\?v=[\w-]{11}$/

export const formSchema = z.object({
  videoUrl: z.string().regex(YOUTUBE_VIDEO_REGEX, {
    message: "Please enter a valid YouTube video URL",
  }),
})

export type FormSchema = typeof formSchema
