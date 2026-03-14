<svelte:head>
  <title>Projects | Qianxi Liu</title>
</svelte:head>

<script lang="ts">
  const projects = [
    {
      title: 'Ghost Marriage',
      href: '/projects/ghost-marriage',
      subtitle: 'Interactive Narrative / Animation / Cultural Critique'
    },
    {
      title: 'AI Museum of Chinese Artifacts',
      href: '/projects/ai-museum',
      subtitle: 'Digital Humanities / AI / Archive / Speculative Heritage'
    },
    {
      title: 'TicSports',
      href: '/projects/ticsports',
      subtitle: 'Interaction Design / Mobile design / UI/UX'
    },
    {
      title: 'TicNote',
      href: '/projects/ticnote',
      subtitle: 'interactive design / UI/UX / Web development'
    }
  ];
</script>

<section class="mx-auto max-w-5xl px-6 py-16 text-white">
  <div class="mb-12">
    <h1 class="text-4xl font-light uppercase tracking-[0.2em]">
      Projects
    </h1>
  </div>

  <div class="flex flex-col gap-6">
    {#each projects as project}
      <a
        href={project.href}
        class="group block border border-white/70 px-8 py-8 transition duration-300 hover:border-white"
      >
        <div class="flex items-center justify-between gap-6">
          <div>
            <h2 class="text-2xl font-light tracking-wide">
              {project.title}
            </h2>
            <p class="mt-3 text-sm font-light tracking-wide text-white/80">
              {project.subtitle}
            </p>
          </div>

          <div class="shrink-0 text-xl font-light tracking-widest transition-transform duration-300 group-hover:translate-x-1">
            →
          </div>
        </div>
      </a>
    {/each}
  </div>
</section>