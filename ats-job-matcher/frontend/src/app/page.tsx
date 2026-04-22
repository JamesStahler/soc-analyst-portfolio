'use client';

import { FormEvent, useState } from 'react';

import { MatchList } from '@/components/MatchList';
import { PricingCard } from '@/components/PricingCard';
import { generateDocs, searchJobs } from '@/lib/api';
import { JobResult } from '@/types';

export default function HomePage() {
  const [matches, setMatches] = useState<JobResult[]>([]);
  const [expandedTitles, setExpandedTitles] = useState<string[]>([]);
  const [resumeText, setResumeText] = useState('');
  const [coverLetterText, setCoverLetterText] = useState('');
  const [status, setStatus] = useState('Ready');

  // Simple client-side usage display. Server should remain source of truth.
  const [usage, setUsage] = useState({ searches: 0, generated: 0, downloads: 0 });

  async function onSearch(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    const formData = new FormData(form);

    const titles = String(formData.get('job_titles') || '').trim();
    if (!titles) {
      setStatus('Please add at least one job title.');
      return;
    }

    setStatus('Searching company career pages...');
    try {
      const data = await searchJobs(formData);
      setMatches(data.matches);
      setExpandedTitles(data.expanded_titles);
      setUsage((prev) => ({ ...prev, searches: prev.searches + 1 }));
      setStatus(`Found ${data.total_matches} high-fit jobs (>=60%).`);
    } catch (err) {
      setStatus(`Search failed: ${(err as Error).message}`);
    }
  }

  async function onGenerate(job: JobResult) {
    if (!resumeText) {
      setStatus('Paste your resume text first for tailoring.');
      return;
    }

    setStatus(`Generating tailored docs for ${job.company}...`);
    try {
      const docs = await generateDocs({
        job_title: job.title,
        company: job.company,
        job_description: job.description,
        base_resume_text: resumeText,
        base_cover_letter_text: coverLetterText,
      });

      // Demo download behavior: create plain text blobs.
      const resumeBlob = new Blob([docs.tailored_resume_text], { type: 'text/plain' });
      const coverBlob = new Blob([docs.tailored_cover_letter_text], { type: 'text/plain' });
      downloadBlob(resumeBlob, `${job.company}-tailored-resume.txt`);
      downloadBlob(coverBlob, `${job.company}-tailored-cover-letter.txt`);

      setUsage((prev) => ({ ...prev, generated: prev.generated + 1, downloads: prev.downloads + 2 }));
      setStatus('Documents generated. Replace text export with PDF/DOCX service in production.');
    } catch {
      setStatus('Document generation failed.');
    }
  }

  return (
    <main className="container grid" style={{ gap: 16 }}>
      <h1>ATS Job Matcher</h1>
      <p className="small">
        Upload your resume, search company career pages only, and generate ATS-optimized documents.
      </p>

      <form className="card grid" onSubmit={onSearch}>
        <h3>Search Inputs</h3>
        <div className="grid two">
          <div>
            <label>Resume (PDF/DOC/DOCX)</label>
            <input name="resume" type="file" accept=".pdf,.doc,.docx" required />
          </div>
          <div>
            <label>Cover Letter (optional)</label>
            <input name="cover_letter" type="file" accept=".pdf,.doc,.docx" />
          </div>
        </div>

        <div className="grid two">
          <div>
            <label>Job Titles (comma-separated)</label>
            <input name="job_titles" placeholder="SOC Analyst, Cybersecurity Analyst" required />
          </div>
          <div>
            <label>Locations (comma-separated)</label>
            <input name="locations" placeholder="Austin, Remote" />
          </div>
        </div>

        <div className="grid two">
          <div>
            <label>Remote</label>
            <select name="remote" defaultValue="false">
              <option value="false">No</option>
              <option value="true">Yes</option>
            </select>
          </div>
          <div>
            <label>Min Match %</label>
            <input name="min_match_score" type="number" defaultValue={60} min={0} max={100} />
          </div>
        </div>

        <button type="submit">Find Matches</button>
      </form>

      <div className="card grid">
        <h3>Resume Content for Tailoring</h3>
        <textarea
          placeholder="Paste resume text for ATS tailoring..."
          rows={8}
          value={resumeText}
          onChange={(e) => setResumeText(e.target.value)}
        />
        <textarea
          placeholder="Paste optional base cover letter text..."
          rows={6}
          value={coverLetterText}
          onChange={(e) => setCoverLetterText(e.target.value)}
        />
      </div>

      {!!expandedTitles.length && (
        <div className="card">
          <h3>Expanded Titles Used</h3>
          <p>{expandedTitles.join(' • ')}</p>
        </div>
      )}

      <div className="card">
        <h3>Matches</h3>
        <MatchList matches={matches} onGenerate={onGenerate} />
      </div>

      <div className="card">
        <h3>Usage Tracking</h3>
        <p className="small">Searches: {usage.searches} | Generated Packages: {usage.generated} | Downloads: {usage.downloads}</p>
      </div>

      <PricingCard />

      <p className="small">Status: {status}</p>
    </main>
  );
}

function downloadBlob(blob: Blob, filename: string) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}
