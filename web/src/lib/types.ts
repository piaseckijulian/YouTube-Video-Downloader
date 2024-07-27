export type ErrorApiResponse = {
  detail:
    | "VIDEO_PRIVATE"
    | "VIDEO_MEMBERS_ONLY"
    | "VIDEO_AGE_RESTRICTED"
    | "VIDEO_REGION_BLOCKED"
    | "VIDEO_LIVE_STREAM"
    | "VIDEO_UNAVAILABLE"
    | "MAX_RETRIES_EXCEEDED"
    | "INVALID_YOUTUBE_URL"
    | "Internal Server Error"
}
