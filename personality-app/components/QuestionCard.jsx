import React from 'react';

export default function QuestionCard({ question, onAnswer }) {
  const handleChange = (e) => {
    onAnswer(e.target.value);
  };

  return (
    <div className="p-4 border rounded-md shadow">
      <p className="mb-2 font-semibold">{question}</p>
      <input
        type="text"
        className="w-full p-2 border"
        onBlur={handleChange}
      />
    </div>
  );
}
