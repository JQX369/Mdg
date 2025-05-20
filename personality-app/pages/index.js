import Link from 'next/link';

export default function Home() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Personality Insight Interview</h1>
      <Link href="/questions" className="text-blue-600 underline">
        Start Interview
      </Link>
    </div>
  );
}
