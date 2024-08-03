export type VideoResponse = {
  videoBase64: string
}

export type ErrorResponse = {
  detail:
    | "VIDEO_PRIVATE"
    | "VIDEO_MEMBERS_ONLY"
    | "VIDEO_AGE_RESTRICTED"
    | "VIDEO_REGION_BLOCKED"
    | "VIDEO_LIVE_STREAM"
    | "VIDEO_UNAVAILABLE"
    | "MAX_RETRIES_EXCEEDED"
    | "INVALID_YOUTUBE_URL"
    | "An unknown error ocurred"
}
