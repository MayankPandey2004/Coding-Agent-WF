'use client';

interface Message {
  type: 'node' | 'tool' | 'code' | 'test' | 'result' | 'error';
  content: string;
  timestamp: number;
}

interface OutputStreamProps {
  messages: Message[];
  loading: boolean;
}

export default function OutputStream({ messages, loading }: OutputStreamProps) {
  const getColor = (type: Message['type']) => {
    switch (type) {
      case 'node':
        return 'text-blue-300';
      case 'tool':
        return 'text-green-300';
      case 'code':
        return 'text-yellow-300';
      case 'test':
        return 'text-purple-300';
      case 'result':
        return 'text-emerald-300';
      case 'error':
        return 'text-red-300';
      default:
        return 'text-slate-300';
    }
  };

  return (
    <div className="bg-slate-800 rounded p-3 h-64 overflow-y-auto text-sm font-mono">
      {messages.length === 0 ? (
        <p className="text-slate-400">Waiting for input...</p>
      ) : (
        <div className="space-y-1">
          {messages.map((msg, i) => (
            <div key={i} className={getColor(msg.type)}>
              {msg.content}
            </div>
          ))}
          {loading && <div className="text-slate-400">Loading...</div>}
        </div>
      )}
    </div>
  );
}
