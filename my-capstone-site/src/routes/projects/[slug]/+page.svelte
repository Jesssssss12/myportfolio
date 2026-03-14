<script lang="ts">
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();

  let overviewOpen = $state(true);
</script>

<svelte:head>
  <title>{data.project.title} | Projects</title>
</svelte:head>

<section class="mx-auto max-w-5xl px-6 py-16 text-white">
  <a
    href="/projects"
    class="mb-10 inline-block text-sm uppercase tracking-[0.2em] text-white/70 transition hover:text-white"
  >
    ← Back to Projects
  </a>

  <div class="mb-12 overflow-hidden ">
    <div class="h-[360px] w-full">
      <img
        src={data.project.image}
        alt={data.project.title}
        class="h-full w-full object-cover"
      />
    </div>
  </div>

  <div class="mb-12  p-8">
    <div class="flex flex-col gap-8 md:flex-row md:items-start md:justify-between">
      <div class="max-w-3xl">
        <p class="mb-3 text-sm uppercase tracking-[0.2em] text-white/70">
          {data.project.year}
        </p>

        <h1 class="text-4xl font-light uppercase tracking-[0.18em]">
          {data.project.title}
        </h1>

        <p class="mt-6 text-lg leading-8">
          {data.project.summary}
        </p>
      </div>

      <div class="min-w-[220px] space-y-4">
        <div>
          <p class="text-sm uppercase tracking-[0.2em] text-white/70">Role</p>
          <p class="mt-2 leading-7">{data.project.role}</p>
        </div>

        <div>
          <p class="text-sm uppercase tracking-[0.2em] text-white/70">Tools</p>
          <ul class="mt-2 space-y-1">
            {#each data.project.tools as tool}
              <li>{tool}</li>
            {/each}
          </ul>
        </div>
      </div>
    </div>
  </div>


  <div class="border border-white/70 p-8">
    <div class="mb-6 flex items-center justify-between">
      <h2 class="text-2xl font-light uppercase tracking-[0.15em]">
        Overview
      </h2>

      
    </div>

    {#if overviewOpen}
      <p class="max-w-3xl leading-8">
        {data.project.overview}
      </p>
    {/if}
  </div>
</section>