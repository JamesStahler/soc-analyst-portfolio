export type JobResult = {
  title: string;
  company: string;
  location?: string | null;
  apply_url: string;
  description: string;
  match_score: number;
  freshness?: string | null;
};

export type SearchResponse = {
  expanded_titles: string[];
  matches: JobResult[];
  total_matches: number;
};
