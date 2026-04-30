<script lang="ts">
  const streamlitUrl = 'https://metdata.streamlit.app';
</script>

<section class="min-h-screen bg-black text-white px-8 py-16">
  <div class="max-w-6xl mx-auto">
    <div class="mb-10">
      <h1 class="text-5xl font-light">Met Chinese Art Dashboard</h1>
      <p class="mt-3 text-white/70">Embed the deployed Streamlit app directly in your Svelte page.</p>
    </div>

    <div class="overflow-hidden rounded-3xl border border-white/10 shadow-2xl bg-white">
      <iframe
        src={streamlitUrl}
        class="w-full min-h-[90vh]"
        frameborder="0"
        loading="lazy"
      ></iframe>
    </div>
  </div>
</section>
