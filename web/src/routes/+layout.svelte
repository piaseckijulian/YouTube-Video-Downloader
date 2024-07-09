<script lang="ts">
  import { inject } from "@vercel/analytics"
  import { injectSpeedInsights } from "@vercel/speed-insights/sveltekit"
  import "../app.css"

  inject()
  injectSpeedInsights()

  const description =
    "YouTube Video Downloader enables quick and easy downloading of YouTube videos."
  const title = "YouTube Video Downloader"
  const url = "https://julian-yt-downloader.vercel.app"
  const imagePath = `${url}/thumbnail.png`
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />

  <meta property="twitter:image" content={imagePath} />
  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:title" content={title} />
  <meta property="twitter:description" content={description} />

  <meta property="og:image" content={imagePath} />
  <meta property="og:site_name" content={title} />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:url" content={url} />
</svelte:head>

<slot />
