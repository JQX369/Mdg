import { useEffect, useState } from 'react';
import PersonalityReport from '../components/PersonalityReport';
import { fetchReport } from '../lib/supabase';

export default function Report() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    fetchReport().then(setReport); // placeholder for DB call
  }, []);

  return (
    <div className="p-4">
      <PersonalityReport report={report} />
    </div>
  );
}
