import { JobResult } from '@/types';

export function MatchList({ matches, onGenerate }: { matches: JobResult[]; onGenerate: (job: JobResult) => void }) {
  if (!matches.length) return <p className="small">No matches yet. Upload and search to begin.</p>;

  return (
    <div className="grid">
      {matches.map((job) => (
        <div key={`${job.company}-${job.apply_url}`} className="card">
          <div className="row">
            <strong>{job.title} · {job.company}</strong>
            <span className="badge">{job.match_score}%</span>
          </div>
          <p className="small">{job.location || 'Location not detected'}</p>
          <div className="matchbar">
            <div className="matchfill" style={{ width: `${job.match_score}%` }} />
          </div>
          <p>{job.description}</p>
          <div className="row">
            <a href={job.apply_url} target="_blank">Direct Apply</a>
            <button onClick={() => onGenerate(job)} style={{ maxWidth: 260 }}>
              Generate ATS Resume + Cover Letter
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}
