import { NextRequest, NextResponse } from 'next/server';

export const runtime = 'nodejs';
export const maxDuration = 300; // 5 min timeout

export async function POST(request: NextRequest) {
  const { task, thread_id } = await request.json();

  if (!task) {
    return NextResponse.json({ error: 'Task is required' }, { status: 400 });
  }

  // Create a readable stream for SSE
  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    async start(controller) {
      try {
        // Call the Python agent backend
        const agentApiUrl = process.env.AGENT_API_URL || 'http://localhost:8000';
        const response = await fetch(⁠ ${agentApiUrl}/agent/stream ⁠, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ task, thread_id }),
        });

        if (!response.ok) {
          const error = await response.text();
          controller.enqueue(encoder.encode(⁠ data: ${JSON.stringify({ error })}\n\n ⁠));
          controller.close();
          return;
        }

        // Stream the response from Python backend
        const reader = response.body?.getReader();
        if (!reader) {
          controller.close();
          return;
        }

        const decoder = new TextDecoder();
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          const text = decoder.decode(value);
          controller.enqueue(encoder.encode(text));
        }

        controller.close();
      } catch (error) {
        const errorMsg = error instanceof Error ? error.message : 'Unknown error';
        controller.enqueue(
          encoder.encode(⁠ data: ${JSON.stringify({ error: errorMsg })}\n\n ⁠)
        );
        controller.close();
      }
    },
  });

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}
