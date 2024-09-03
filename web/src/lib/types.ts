export type VideoResponse = {
  videoBase64: string
}

export type ErrorResponse = {
  detail: "VIDEO_UNAVAILABLE" | string
}
