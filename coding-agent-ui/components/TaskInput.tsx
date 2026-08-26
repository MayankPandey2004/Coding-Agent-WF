'use client';

import { useState } from 'react';
import { Play } from 'lucide-react';

interface TaskInputProps {
  onRun: (task: string) => void;
  loading: boolean;
}

export default function TaskInput({ onRun, loading }: TaskInputProps) {
  const [input, setInput] = useState('');

  const handleSubmit = () => {
    onRun(input);
    setInput('');
  };

  return (
    <div className="bg-slate-700 rounded-lg p-4 border border-slate-600">
      <label className="block text-white font-semibold mb-3">Task</label>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Example: write a function that reverses a string..."
        className="w-full bg-slate-600 text-white border border-slate-500 rounded p-3 mb-3 h-24"
        disabled={loading}
      />

      <button
        onClick={handleSubmit}
        disabled={loading || !input.trim()}
        className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg disabled:opacity-50"
      >
        <Play size={16} />
        {loading ? 'Running...' : 'Run'}
      </button>
    </div>
  );
}
