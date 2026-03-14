<script lang="ts">
  const projects = [
    {
      title: 'Ghost Marriage',
      href: '/projects/ghost-marriage',
      summary: 'An interactive narrative and animation project based on Chinese ghost marriage culture.',
      image: '/images/ghost-marriage.png'
    },
    {
      title: 'AI Museum of Chinese Artifacts',
      href: '/projects/ai-museum',
      summary: 'A digital humanities and AI project exploring generated Chinese artifacts and museum narratives.',
      image: '/images/ai-museum.png'
    },
    {
      title: 'TicSports',
      href: '/projects/ticsports',
      summary: 'An AI-supported sports and treadmill experience focused on tracking, coaching, and interface design.',
      image: '/images/ticsports.jpg'
    },
    {
      title: 'Capstone Portfolio Site',
      href: '/projects/capstone-site',
      summary: 'A personal academic portfolio built with SvelteKit, Tailwind, and TypeScript.',
      image: '/images/capstone-site.jpg'
    }
  ];
</script>

<svelte:head>
  <title>Projects</title>
</svelte:head>

<section class="space-y-8">
  <div>
    <p class="text-sm text-gray-500">Work</p>
    <h1 class="mt-2 text-4xl font-bold">Selected Projects</h1>
    <p class="mt-4 max-w-2xl text-gray-600">
      A selection of projects across interactive storytelling, digital humanities,
      interface design, and creative technology.
    </p>
  </div>

  <div class="grid gap-6 md:grid-cols-2">
    {#each projects as project}
      <a
        href={project.href}
        class="block overflow-hidden rounded-2xl border bg-white shadow-sm hover:shadow-md"
      >
        <div class="h-56 w-full bg-pink-50">
          <img
            src={project.image}
            alt={project.title}
            class="h-full w-full object-cover"
          />
        </div>

        <div class="p-5">
          <h2 class="text-xl font-semibold">{project.title}</h2>
          <p class="mt-3 text-sm leading-6 text-gray-600">
            {project.summary}
          </p>
          <p class="mt-4 text-sm font-medium">View Project →</p>
        </div>
      </a>
    {/each}
  </div>
</section>