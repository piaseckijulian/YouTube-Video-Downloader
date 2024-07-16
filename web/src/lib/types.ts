export type ErrorApiResponse = {
  detail:
    | "VIDEO_PRIVATE"
    | "VIDEO_MEMBERS_ONLY"
    | "VIDEO_AGE_RESTRICTED"
    | "VIDEO_REGION_BLOCKED"
    | "VIDEO_LIVE_STREAM"
    | "VIDEO_UNAVAILABLE"
    | "TOO_MANY_REQUESTS"
    | "The provided URL is not a valid YouTube video URL"
    | "An unexpected error ocurred"
}
