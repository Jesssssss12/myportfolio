<script lang="ts">
  import '../app.css';
</script>

<header class="border-b">
  <div class="mx-auto max-w-6xl flex items-center justify-between p-4">
    <a href="/" class="text-xl font-bold">Qianxi Liu</a>

    <nav class="flex gap-6 text-sm">
      <a href="/" class="hover:underline">Home</a>
      <a href="/about" class="hover:underline">About</a>
      <a href="/cv" class="hover:underline">CV</a>
      <a href="/projects" class="hover:underline">Projects</a>
    </nav>
  </div>
</header>

<main class="mx-auto max-w-6xl p-6">
  <slot />
</main>