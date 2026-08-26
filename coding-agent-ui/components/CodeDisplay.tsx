'use client';

import { Copy, Check } from 'lucide-react';
import { useState } from 'react';

interface CodeDisplayProps {
  code: string;
}

export default function CodeDisplay({ code }: CodeDisplayProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="bg-slate-700 rounded-lg p-4 border border-slate-600">
      <div className="flex justify-between items-center mb-3">
        <h2 className="text-white font-semibold">Generated Code</h2>
        <button
          onClick={handleCopy}
          className="flex items-center gap-2 px-3 py-1 bg-slate-600 hover:bg-slate-500 text-white rounded text-sm"
        >
          {copied ? <Check size={16} /> : <Copy size={16} />}
          {copied ? 'Copied' : 'Copy'}
        </button>
      </div>

      <pre className="bg-slate-800 rounded p-3 overflow-x-auto text-slate-200 text-sm">
        <code>{code}</code>
      </pre>
    </div>
  );
}
