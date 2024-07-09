<script lang="ts">
  import DownloadErrors from "$lib/components/DownloadErrors.svelte"
  import DownloadForm from "$lib/components/DownloadForm.svelte"
  import DownloadLink from "$lib/components/DownloadLink.svelte"

  import type { ActionData, PageData } from "./$types"

  export let data: PageData
  export let form: ActionData
</script>

<main class="container mt-10">
  <h1 class="mb-5 text-center text-5xl font-bold">
    <span class="text-primary">YouTube</span> Video Downloader
  </h1>

  <DownloadForm data={data.form} />

  {#if form?.videoBase64String}
    <DownloadLink videoBase64String={form.videoBase64String} />
  {/if}

  {#if form?.error}
    <DownloadErrors error={form.error} />
  {/if}
</main>
