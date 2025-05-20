import React from 'react';

export default function PersonalityReport({ report }) {
  if (!report) return null;

  return (
    <div className="space-y-4">
      <h2 className="text-xl font-bold">Personality Report</h2>
      <pre className="whitespace-pre-wrap">{JSON.stringify(report, null, 2)}</pre>
    </div>
  );
}
