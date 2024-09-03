<script lang="ts">
  import type { ErrorResponse } from "$lib/types"
  import ErrorMessage from "./ErrorMessage.svelte"

  export let error: ErrorResponse["detail"]
</script>

{#if error === "VIDEO_UNAVAILABLE"}
  <ErrorMessage message="Video is unavailable" />
{:else if error}
  <ErrorMessage message="An unknown error ocurred" />
{/if}
