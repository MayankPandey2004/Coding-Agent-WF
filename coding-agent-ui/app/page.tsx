'use client';

import { useState, useRef, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import TaskInput from '@/components/TaskInput';
import OutputStream from '@/components/OutputStream';
import CodeDisplay from '@/components/CodeDisplay';
import SessionHistory from '@/components/SessionHistory';

interface Message {
  type: 'node' | 'tool' | 'code' | 'test' | 'result' | 'error';
  content: string;
  timestamp: number;
}

// Mock agent responses for testing without backend
const MOCK_RESPONSES: Record<string, Message[]> = {
  'write a function that reverses a string': [
    { type: 'node', content: '[PLANNER] Planning task...', timestamp: Date.now() },
    { type: 'node', content: '[CODER] Writing code...', timestamp: Date.now() + 500 },
    { type: 'tool', content: 'Tool: write_file (eval_reverse.py)', timestamp: Date.now() + 1000 },
    { type: 'code', content: 'def reverse_string(s):\n  return s[::-1]', timestamp: Date.now() + 1500 },
    { type: 'tool', content: 'Tool: run_tests', timestamp: Date.now() + 2000 },
    { type: 'test', content: 'Test passed: reverse_string("hello") == "olleh"', timestamp: Date.now() + 2500 },
    { type: 'node', content: '[EVALUATOR] All tests passed!', timestamp: Date.now() + 3000 },
    { type: 'result', content: 'Task completed successfully', timestamp: Date.now() + 3500 },
  ],
};

export default function Home() {
  const [task, setTask] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [threadId, setThreadId] = useState<string>('');
  const [generatedCode, setGeneratedCode] = useState('');
  const [attempts, setAttempts] = useState(0);
  const [toolCalls, setToolCalls] = useState(0);
  const [duration, setDuration] = useState(0);
  const [success, setSuccess] = useState<boolean | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setThreadId(uuidv4());
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleRun = async (taskText: string) => {
    if (!taskText.trim()) return;

    setTask(taskText);
    setMessages([]);
    setLoading(true);
    setGeneratedCode('');
    setAttempts(0);
    setToolCalls(0);
    setDuration(0);
    setSuccess(null);

    const startTime = Date.now();

    // Use mock data for testing
    const mockMessages = MOCK_RESPONSES[taskText.toLowerCase()] || [
      { type: 'node', content: '[PLANNER] Planning...', timestamp: Date.now() },
      { type: 'error', content: 'Backend not connected. Using mock data.', timestamp: Date.now() + 500 },
      { type: 'node', content: '[CODER] Writing...', timestamp: Date.now() + 1000 },
      { type: 'tool', content: 'Tool: write_file', timestamp: Date.now() + 1500 },
      { type: 'result', content: 'Task completed', timestamp: Date.now() + 2000 },
    ];

    // Simulate streaming
    for (let i = 0; i < mockMessages.length; i++) {
      await new Promise(resolve => setTimeout(resolve, 300));

      const msg = mockMessages[i];
      setMessages(prev => [...prev, msg]);

      if (msg.type === 'tool') {
        setToolCalls(prev => prev + 1);
      }
      if (msg.type === 'code') {
        setGeneratedCode('def reverse_string(s):\n  return s[::-1]\n\n# Test\nassert reverse_string("hello") == "olleh"');
      }
      if (msg.type === 'result') {
        setAttempts(prev => prev + 1);
        setSuccess(true);
      }
    }

    setLoading(false);
    setDuration(Math.round((Date.now() - startTime) / 1000));
  };

  const handleNewSession = () => {
    setThreadId(uuidv4());
    setMessages([]);
    setTask('');
    setGeneratedCode('');
    setAttempts(0);
    setToolCalls(0);
    setDuration(0);
    setSuccess(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <div className="max-w-7xl mx-auto p-4">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">CodeSmith</h1>
          <p className="text-slate-400">AI-powered autonomous coding agent</p>
          <p className="text-xs text-yellow-500 mt-2">Demo mode (mock data - backend not connected)</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
          <div className="lg:col-span-1">
            <SessionHistory threadId={threadId} onNewSession={handleNewSession} />
          </div>

          <div className="lg:col-span-3 space-y-4">
            <TaskInput onRun={handleRun} loading={loading} />

            {(attempts > 0 || toolCalls > 0 || duration > 0) && (
              <div className="bg-slate-700 rounded-lg p-4 border border-slate-600">
                <div className="grid grid-cols-3 gap-4 text-center">
                  <div>
                    <p className="text-slate-400 text-sm">Attempts</p>
                    <p className="text-2xl font-bold text-blue-400">{attempts}</p>
                  </div>
                  <div>
                    <p className="text-slate-400 text-sm">Tool Calls</p>
                    <p className="text-2xl font-bold text-green-400">{toolCalls}</p>
                  </div>
                  <div>
                    <p className="text-slate-400 text-sm">Duration</p>
                    <p className="text-2xl font-bold text-purple-400">{duration}s</p>
                  </div>
                </div>
              </div>
            )}

            {success !== null && (
              <div className={`p-4 rounded-lg ${success ? 'bg-green-900 border border-green-600 text-green-200' : 'bg-red-900 border border-red-600 text-red-200'}`}>
                {success ? 'Task completed successfully!' : 'Task failed'}
              </div>
            )}

            <div className="bg-slate-700 rounded-lg p-4 border border-slate-600">
              <h2 className="text-white font-semibold mb-3">Output</h2>
              <OutputStream messages={messages} loading={loading} />
              <div ref={messagesEndRef} />
            </div>

            {generatedCode && <CodeDisplay code={generatedCode} />}
          </div>
        </div>
      </div>
    </div>
  );
}
