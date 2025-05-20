import { useState } from 'react';
import QuestionCard from '../components/QuestionCard';
import PaymentButton from '../components/PaymentButton';
import { sendAnswer } from '../lib/openai';

const questions = [
  'Stress reactivity & resilience',
  // ... add remaining questions here
];

export default function Questions() {
  const [current, setCurrent] = useState(0);
  const [responses, setResponses] = useState({});

  const handleAnswer = async (answer) => {
    const question = questions[current];
    setResponses({ ...responses, [question]: answer });
    await sendAnswer(question, answer); // placeholder integration
    if (current < questions.length - 1) {
      setCurrent(current + 1);
    }
  };

  return (
    <div className="p-4 space-y-4">
      {current < questions.length ? (
        <QuestionCard
          question={questions[current]}
          onAnswer={handleAnswer}
        />
      ) : (
        <div className="space-y-2">
          <p>All questions answered.</p>
          <PaymentButton onClick={() => alert('TODO: implement payment')} />
        </div>
      )}
    </div>
  );
}
