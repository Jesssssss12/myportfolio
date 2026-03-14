<script lang="ts">
  let current = $state(0);

  const images = [
    "/images/ai-museum.png",
    "/images/ghost-marriage.png",
    "/images/ticsports.png",
    "/images/ticnote.png"
  ];

  setInterval(() => {
    current = (current + 1) % images.length;
  }, 3000);
</script>

<svelte:head>
  <title>Home | My Capstone Site</title>
</svelte:head>

<section class="relative flex min-h-[80vh] items-center justify-center text-center text-white">

  <!-- background images -->
  {#each images as img, index}
    <div
      class="absolute inset-0 bg-cover bg-center transition-opacity duration-1000"
      style="background-image: url('{img}')"
      class:opacity-100={index === current}
      class:opacity-0={index !== current}
    ></div>
  {/each}

  <!-- overlay -->
  <div class="absolute inset-0 bg-black/50"></div>

  <!-- text content -->
  <div class="relative z-10 max-w-3xl px-6">

    <p class="text-sm uppercase tracking-widest text-gray-300">
      Academic Profile
    </p>

    <h1 class="mt-4 text-5xl font-bold">
      Hi, I'm Qianxi Liu
    </h1>

    <p class="mt-6 text-lg text-gray-200">
      I am a digital media and humanities student interested in interactive
      storytelling, interface design, and AI-supported creative practice.
    </p>

  </div>

</section>