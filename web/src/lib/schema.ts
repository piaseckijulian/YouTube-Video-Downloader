import { z } from "zod"

const YOUTUBE_VIDEO_REGEX =
  /\b(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|e\/|shorts\/|live\/|attribution_link\?a=|oembed\?url=|player_embedded\?v=|v\/)|youtu\.be\/|youtube-nocookie\.com\/embed\/|youtube\.com\/v\/|youtube\.com\/v\/|youtube\.com\/shorts\/|youtube\.com\/live\/|youtube\.com\/embed\/|youtube\.com\/watch\?v=|youtube\.com\/attribution_link\?a=|youtube\.com\/player_embedded\?v=|youtube\.com\/oembed\?url=|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})(?:\S*)?\b/

export const formSchema = z.object({
  videoUrl: z.string().regex(YOUTUBE_VIDEO_REGEX, {
    message: "Please enter a valid YouTube video URL",
  }),
})

export type FormSchema = typeof formSchema
