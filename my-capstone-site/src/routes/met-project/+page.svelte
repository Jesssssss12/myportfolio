<script lang="ts">
  import { onMount } from 'svelte';

  type Artwork = {
    year: number;
    Classification: string;
    'Object Name': string;
    'Artist Display Name': string;
    Dynasty: string;
  };

  let data: Artwork[] = [];
  let showAll = false;

  const chartId = 'met-chart';

  async function loadData() {
    const res = await fetch('/data/met_cleaned.json');
    data = await res.json();
    await drawChart();
  }

  async function drawChart() {
    const Plotly = await import('plotly.js-dist-min');

    const groups: Record<string, Artwork[]> = {};

    data.forEach((d) => {
      const key = d.Classification || 'Unknown';
      if (!groups[key]) groups[key] = [];
      groups[key].push(d);
    });

    const traces = Object.entries(groups).map(([key, items]) => ({
      x: items.map((d) => d.year),
      y: items.map(() => key),
      mode: 'markers+lines',
      type: 'scatter',
      name: key,
      visible: showAll ? true : 'legendonly',
      line: {
        width: 0
      },
      marker: {
        size: 8,
        opacity: 0.7
      },
      customdata: items.map((d) => [
        d['Object Name'],
        d['Artist Display Name'],
        d.Dynasty
      ]),
      hovertemplate:
        '<b>%{customdata[0]}</b><br>' +
        'Classification: %{y}<br>' +
        'Year: %{x}<br>' +
        'Artist: %{customdata[1]}<br>' +
        'Dynasty: %{customdata[2]}<extra></extra>'
    }));

    const layout = {
      height: 760,
      paper_bgcolor: '#000000',
      plot_bgcolor: '#000000',

      font: {
        family: 'Inter, system-ui, sans-serif',
        color: '#e5e5e5',
        size: 13
      },

      xaxis: {
        title: {
          text: 'Year',
          font: {
            family: 'Inter, system-ui, sans-serif',
            size: 12,
            color: '#bdbdbd'
          }
        },
        range: [0, 2025],
        tickformat: 'd',
        tickfont: {
          family: 'Inter, system-ui, sans-serif',
          size: 11,
          color: '#d4d4d4'
        },
        gridcolor: 'rgba(255,255,255,0.06)',
        zerolinecolor: 'rgba(255,255,255,0.2)',

        rangeslider: {
          visible: true,
          bgcolor: 'rgba(255,255,255,0.06)',
          bordercolor: 'rgba(255,255,255,0.22)',
          borderwidth: 1,
          thickness: 0.1
        }
      },

      yaxis: {
        title: null,
        automargin: true,
        tickfont: {
          family: 'Inter, system-ui, sans-serif',
          size: 12,
          color: '#e5e5e5'
        },
        gridcolor: 'rgba(255,255,255,0.08)',
        zerolinecolor: 'rgba(255,255,255,0.15)'
      },

      legend: {
        title: {
          text: 'Click to Show Classification',
          font: {
            family: 'Inter, system-ui, sans-serif',
            size: 12,
            color: '#e5e5e5'
          }
        },
        font: {
          family: 'Inter, system-ui, sans-serif',
          size: 11,
          color: '#bdbdbd'
        }
      },

      margin: {
        l: 150,
        r: 40,
        t: 20,
        b: 90
      }
    };

    await Plotly.default.newPlot(chartId, traces, layout, {
      responsive: true,
      displayModeBar: true
    });
  }

  async function toggle() {
    showAll = !showAll;
    await drawChart();
  }

  onMount(loadData);
</script>

<svelte:head>
  <title>Met Dashboard</title>
</svelte:head>

<section class="mx-auto max-w-6xl px-6 py-16 space-y-16 text-white">
  <div>
    <h1 class="text-5xl font-light tracking-widest uppercase mb-6">
      Met Chinese Art
    </h1>

    <p class="max-w-3xl leading-7 text-white/70">
     This project uses the Metropolitan Museum of Art’s Open Access dataset to examine patterns in the collection of Chinese art, focusing on both time distribution and object classification. Through an interactive visualization, artworks are mapped by year and categorized by type, allowing users to explore how different forms—such as ceramics, textiles, and paintings—are distributed across historical periods. By combining temporal trends with categorical distinctions, the dashboard reveals potential concentrations or gaps in the collection, offering insight into how Chinese art may be selectively represented within a Western museum context.

    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    <div class="border border-white/20 p-6">
      <p class="text-sm uppercase tracking-widest text-white/50 mb-3">
        Data Source
      </p>
      <p class="text-2xl font-light">
        https://metmuseum.github.io/
      </p>
    </div>

    <div class="border border-white/20 p-6">
      <p class="text-sm uppercase tracking-widest text-white/50 mb-3">
        Processing
      </p>
      <p class="text-2xl font-light">
        Python
      </p>
    </div>

    <div class="border border-white/20 p-6">
      <p class="text-sm uppercase tracking-widest text-white/50 mb-3">
        Interface
      </p>
      <p class="text-2xl font-light">
        Svelte + Tailwind
      </p>
    </div>
  </div>

  <div>
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-4xl font-light tracking-widest uppercase">
        Visualization
      </h2>

      <button
        on:click={toggle}
        class="border border-white/30 px-5 py-2 text-sm uppercase tracking-widest hover:bg-white hover:text-black transition"
      >
        {showAll ? 'Hide All' : 'Show All'}
      </button>
    </div>

    <div class="border border-white/20 p-6">
      <div id={chartId}></div>
    </div>
  </div>

</section>

<style>
  :global(body) {
    background-color: #000;
  }

  :global(.modebar) {
    filter: invert(1);
    opacity: 0.7;
  }

  :global(.rangeslider .scatterlayer path),
  :global(.rangeslider .points),
  :global(.rangeslider .point) {
    display: none !important;
    opacity: 0 !important;
  }

  :global(.rangeslider .plot),
  :global(.rangeslider .rangeplot) {
    fill: rgba(255, 255, 255, 0.06);
  }

  :global(.rangeslider rect) {
    stroke: rgba(255, 255, 255, 0.25);
  }

  :global(.rangeslider .handle) {
    fill: #d4d4d4;
    stroke: #d4d4d4;
  }
</style>