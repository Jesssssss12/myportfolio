<script lang="ts">
  import { onMount } from 'svelte';

  let data: any[] = [];
  let categoryData: any[] = [];
  let periodData: any[] = [];

  function parseCSV(text: string) {
    const lines = text.trim().split('\n');
    const headers = lines[0].split(',');

    return lines.slice(1).map(line => {
      const values = line.split(',');
      const row: any = {};
      headers.forEach((h, i) => row[h] = values[i]);
      return row;
    });
  }

  function getPeriod(year: number) {
    if (!year) return 'Unknown';
    if (year < 1400) return 'Before 1400';
    if (year < 1600) return '1400–1599';
    if (year < 1800) return '1600–1799';
    if (year < 1912) return '1800–1911';
    return 'After 1912';
  }

  onMount(async () => {
    const res = await fetch('/data/Met_database.csv');
    const text = await res.text();

    data = parseCSV(text).filter(d => d.Culture?.includes('China'));

    // 分类统计
    const cat: any = {};
    data.forEach(d => {
      const c = d.Classification || 'Unknown';
      cat[c] = (cat[c] || 0) + 1;
    });

    categoryData = Object.entries(cat).map(([k, v]) => ({
      name: k,
      count: v
    }));

    // 时间统计
    const time: any = {};
    data.forEach(d => {
      const y = Number(d.year);
      const p = getPeriod(y);
      time[p] = (time[p] || 0) + 1;
    });

    periodData = Object.entries(time).map(([k, v]) => ({
      period: k,
      count: v
    }));
  });
</script>

<section class="min-h-screen bg-black text-white px-8 py-16">
  <div class="max-w-5xl mx-auto">

    <h1 class="text-5xl font-light mb-10">
      Met Chinese Art Collection
    </h1>

    <!-- 时间 -->
    <div class="mb-16">
      <h2 class="text-2xl mb-4">Time Distribution</h2>

      {#each periodData as item}
        <div class="mb-3">
          <div class="flex justify-between text-sm text-white/60">
            <span>{item.period}</span>
            <span>{item.count}</span>
          </div>

          <div class="h-4 bg-white/10 rounded">
            <div
              class="h-full bg-white"
              style="width: {item.count / 2000 * 100}%"
            ></div>
          </div>
        </div>
      {/each}
    </div>

    <!-- 分类 -->
    <div>
      <h2 class="text-2xl mb-4">Category Distribution</h2>

      <div class="grid grid-cols-2 gap-4">
        {#each categoryData as item}
          <div class="border border-white/20 p-4 rounded">
            <p class="text-sm text-white/50">{item.name}</p>
            <p class="text-xl">{item.count}</p>
          </div>
        {/each}
      </div>
    </div>

  </div>
</section>