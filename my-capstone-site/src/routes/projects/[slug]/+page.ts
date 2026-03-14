import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { projects } from '$lib/data/projects';

export const load: PageLoad = ({ params }) => {
  const project = projects.find((item) => item.slug === params.slug);

  if (!project) {
    throw error(404, 'Project not found');
  }

  return { project };
};