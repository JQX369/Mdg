import React from 'react';

export default function PaymentButton({ onClick }) {
  return (
    <button
      className="px-4 py-2 text-white bg-blue-600 rounded"
      onClick={onClick}
    >
      Pay Now
    </button>
  );
}
