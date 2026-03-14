export type Project = {
  slug: string;
  title: string;
  year: string;
  role: string;
  tools: string[];
  summary: string;
  overview: string;
  image: string;
};

export const projects: Project[] = [
  {
    slug: 'ghost-marriage',
    title: 'Ghost Marriage',
    year: '2025',
    role: 'Interactive Narrative / Animation / Cultural Critique',
    tools: ['Blender', 'Animation', 'Storytelling', 'Interactive Media'],
    summary:
      'An interactive narrative and animation project based on the historical practice of ghost marriage in China.',
    overview:
      'Ghost Marriage is a multimedia storytelling project that explores the unequal treatment and tragic fate of women within patriarchal traditions. The project combines narrative design, visual atmosphere, and cultural critique to build an emotionally immersive experience.',
    image: '/images/ghost-marriage.png'
  },
  {
    slug: 'ai-museum',
    title: 'AI Museum of Chinese Artifacts',
    year: '2025',
    role: 'Digital Humanities / AI / Archive / Speculative Heritage',
    tools: ['AI Image Generation', 'Metadata', 'Digital Humanities', 'Research'],
    summary:
      'A speculative digital humanities project exploring AI-generated Chinese artifacts and museum narratives.',
    overview:
      'This project investigates how AI can reinterpret cultural heritage through synthetic artifacts and speculative museum interfaces. Using Chinese artifact references and digital humanities methods, it asks how authenticity, authorship, and displacement are reshaped by generative systems.',
    image: '/images/ai-museum.png'
  },
  {
    slug: 'ticsports',
    title: 'TicSports',
    year: '2025',
    role: 'Interaction Design / Product Thinking / AI-supported Experience',
    tools: ['Figma', 'Interaction Design', 'Product Design', 'AI UX'],
    summary:
      'TicSports is a product-focused design project centered on building a more intelligent and engaging fitness experience. The design explores how AI can support exercise habits through adaptive interfaces, feedback systems, and personalized interaction.',
    overview:
      'The project focuses on balancing data visibility, motivation, and usability across both hardware and software touchpoints, while maintaining a clear and intuitive interaction flow.',
    image: '/images/ticsports.png'
  },
  {
    slug: 'ticnote',
    title: 'TicNote',
    year: '2025',
    role: 'AI Product Design / Interaction Design / Hardware-Software Integration',
    tools: ['Product Design', 'AI Interaction', 'UX Research', 'Prototyping'],
    summary:
      'TicNote is an AI-supported voice note and knowledge capture tool designed to transform spoken ideas into structured information.',
    overview:
      'The project explores how AI can assist users in capturing thoughts, meetings, and ideas through voice interaction. By combining speech recognition, summarization, and structured note generation, TicNote aims to create a more fluid and natural knowledge recording experience.',
    image: '/images/ticnote.png'
  }
];