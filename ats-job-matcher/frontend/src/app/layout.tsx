import './globals.css';
import { ReactNode } from 'react';

export const metadata = {
  title: 'ATS Job Matcher',
  description: 'Find high-fit career-page jobs and generate ATS-optimized documents.',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
