<script lang="ts">
  import type { ApiError } from "$lib/types"
  import Error from "./Error.svelte"

  export let error: ApiError
</script>

{#if error === "VIDEO_UNAVAILABLE"}
  <Error message="Video is unavailable" />
{:else if error === "VIDEO_LIVE_STREAM"}
  <Error message="Video is a Live Stream" />
{:else if error === "VIDEO_AGE_RESTRICTED"}
  <Error message="Video is Age Restricted" />
{:else if error === "VIDEO_BLOCKED_REGION"}
  <Error message="Video is blocked in your region" />
{:else if error === "VIDEO_MEMBERS_ONLY"}
  <Error message="Video is only for members" />
{:else if error === "VIDEO_PRIVATE"}
  <Error message="Video is private" />
{:else if error}
  <Error message="Something went wrong" />
{/if}
