<script lang="ts">
  let showMore = $state(false);
</script>

<svelte:head>
  <title>Home | My Capstone Site</title>
</svelte:head>

<section class="mx-auto max-w-6xl px-6 py-16">
  <div class="grid gap-10 md:grid-cols-2 md:items-center">
    <div>
      <p class="text-sm font-medium text-muted-foreground">Academic Profile</p>
      <h1 class="mt-3 text-4xl font-bold tracking-tight md:text-5xl">
        Hi, I'm Qianxi Liu
      </h1>
      <p class="mt-5 text-lg leading-8 text-muted-foreground">
        I am a digital media and humanities student interested in interactive storytelling,
        interface design, and AI-supported creative practice.
      </p>

    

      <div class="mt-8">
      
        {#if showMore}
          <div class="mt-4 rounded-xl border bg-card p-4 shadow-sm">
            <p class="text-sm text-muted-foreground">
              This site presents my background, education, skills, and selected projects.
              It is built with SvelteKit, TypeScript, Tailwind CSS, and shadcn-svelte.
            </p>
          </div>
        {/if}
      </div>
    </div>

  </div>
</section>