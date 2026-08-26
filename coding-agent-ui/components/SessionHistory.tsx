'use client';

interface SessionHistoryProps {
  threadId: string;
  onNewSession: () => void;
}

export default function SessionHistory({ threadId, onNewSession }: SessionHistoryProps) {
  return (
    <div className="bg-slate-700 rounded-lg p-4 border border-slate-600">
      <h2 className="text-white font-semibold mb-3">Session</h2>
      <p className="text-slate-300 text-sm mb-3">
        <span className="text-slate-400">ID:</span>
        <br />
        <code className="text-xs text-slate-200 break-all">{threadId}</code>
      </p>
      <button
        onClick={onNewSession}
        className="w-full px-3 py-2 bg-slate-600 hover:bg-slate-500 text-white rounded text-sm"
      >
        New Session
      </button>
    </div>
  );
}
