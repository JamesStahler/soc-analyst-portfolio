import { SearchResponse } from '@/types';

const API = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1';

export async function searchJobs(formData: FormData): Promise<SearchResponse> {
  const res = await fetch(`${API}/jobs/search`, {
    method: 'POST',
    body: formData,
  });

  if (!res.ok) {
    const detail = await res.text();
    throw new Error(detail || 'Search failed');
  }

  return res.json();
}

export async function generateDocs(payload: {
  job_title: string;
  company: string;
  job_description: string;
  base_resume_text: string;
  base_cover_letter_text?: string;
}) {
  const res = await fetch(`${API}/documents/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!res.ok) throw new Error('Generation failed');
  return res.json();
}
