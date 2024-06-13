export type ApiError =
  | 'VIDEO_UNAVAILABLE'
  | 'VIDEO_PRIVATE'
  | 'VIDEO_MEMBERS_ONLY'
  | 'VIDEO_AGE_RESTRICTED'
  | 'VIDEO_BLOCKED_REGION'
  | 'VIDEO_LIVE_STREAM';

export interface ApiErrorRes {
  error: ApiError;
}
