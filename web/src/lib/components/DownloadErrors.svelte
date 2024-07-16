<script lang="ts">
  import type { ErrorApiResponse } from "$lib/types"
  import ErrorMessage from "./ErrorMessage.svelte"

  export let error: ErrorApiResponse["detail"]
</script>

{#if error === "VIDEO_UNAVAILABLE"}
  <ErrorMessage message="Video is unavailable" />
{:else if error === "VIDEO_LIVE_STREAM"}
  <ErrorMessage message="Video is a Live Stream" />
{:else if error === "VIDEO_AGE_RESTRICTED"}
  <ErrorMessage message="Video is Age Restricted" />
{:else if error === "VIDEO_REGION_BLOCKED"}
  <ErrorMessage message="Video is blocked in your region" />
{:else if error === "VIDEO_MEMBERS_ONLY"}
  <ErrorMessage message="Video is only for members" />
{:else if error === "VIDEO_PRIVATE"}
  <ErrorMessage message="Video is private" />
{:else if error === "TOO_MANY_REQUESTS"}
  <ErrorMessage message="Too many requests. Try again later." />
{:else if error}
  <ErrorMessage message="Something went wrong" />
{/if}
