<script lang="ts">
  import { onMount } from "svelte"

  export let videoBase64: string

  let downloadAnchorRef: HTMLAnchorElement

  onMount(() => {
    const arrayBuffer = new Uint8Array(
      atob(videoBase64)
        .split("")
        .map((char) => char.charCodeAt(0)),
    ).buffer

    const blob = new Blob([arrayBuffer], { type: "video/mp4" })

    downloadAnchorRef.href = URL.createObjectURL(blob)
    downloadAnchorRef.click()
  })
</script>

<div class="flex justify-center">
  <a
    href="/"
    download="video.mp4"
    class="hover:text-primary mt-3 text-2xl font-semibold transition-all"
    bind:this={downloadAnchorRef}
  >
    Click here to download
  </a>
</div>
