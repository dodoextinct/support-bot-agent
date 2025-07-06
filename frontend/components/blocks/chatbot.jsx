'use client';

import React, { useState } from 'react';
import { CanvasRevealEffect } from '@/components/ui/canvas-effect';
import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { ScrollArea } from '@/components/ui/scroll-area';
import { BotIcon, LoaderIcon, PlusIcon, Send, SendHorizonalIcon, SendHorizontalIcon, SendIcon, SendToBackIcon } from 'lucide-react';
import { Card } from '../ui/card';
import { marked } from 'marked';
import { Textarea } from '../ui/textarea';

export function Chatbot() {
    const [hovered, setHovered] = useState(false);
    const [query, setQuery] = useState('');
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const sendQuery = async (e) => {
        e.preventDefault();
        if (!query.trim()) return;

        const userMessage = { role: 'user', content: query };
        setMessages((prev) => [...prev, userMessage]);
        setQuery('');
        setLoading(true);

        try {
            const res = await fetch('http://localhost:8000/support', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: query }),
            });

            const data = await res.json();
            const botMessage = {
                role: 'assistant',
                content: data.message || 'No response.',
            };
            setMessages((prev) => [...prev, botMessage]);
        } catch (err) {
            console.error('Error fetching support response:', err);
            setMessages((prev) => [
                ...prev,
                { role: 'assistant', content: 'Something went wrong.' },
            ]);
        }

        setLoading(false);
    };

    return (
        <div className="h-[90vh] w-screen">
            <Card
                onMouseEnter={() => setHovered(true)}
                onMouseLeave={() => setHovered(false)}
                className="flex mx-auto  w-full h-full items-center justify-center overflow-hidden"
            >
                <div className="relative flex w-full h-full items-center justify-center p-4">

                    <div className="flex flex-col justify-between z-20 w-full h-full">

                        <ScrollArea className="w-full h-full overflow-auto p-1">
                            <h1 className="flex items-center space-x-10 select-none justify-center py-2 text-center text-2xl font-extrabold tracking-tight md:text-4xl">
                                <BotIcon className='w-10 h-10' />  <div className="bg-gradient-to-r from-yellow-500 to-yellow-600 bg-clip-text text-transparent">
                                    Chat Support
                                </div>
                            </h1>
                            <p className="mx-auto mb-4 text-center text-xs text-primary/60">
                                Shoot your queries.
                            </p>
                            <div className="px-6">


                                {messages.map((msg, idx) => (
                                    <div
                                        key={idx}
                                        className={cn(
                                            'flex my-4 rounded-md px-4 py-2 text-sm',
                                            msg.role === 'user'
                                                ? 'bg-gray-100 text-left dark:bg-gray-800'
                                                : 'bg-yellow-100 text-left dark:bg-slate-900'
                                        )}
                                    >
                                        <div className='w-10'>{msg.role === 'user' ? 'You' : 'AI'}:</div>
                                        {msg.role === 'user' ? (
                                            <div>{msg.content}</div>
                                        ) : (
                                            <div
                                                className="prose prose-sm dark:prose-invert"
                                                dangerouslySetInnerHTML={{ __html: marked(msg.content) }}
                                            />
                                        )}
                                    </div>
                                ))}


                                {loading && (
                                    <div className="flex items-center space-x-2 my-2 animate-pulse rounded-md bg-muted p-4 text-sm text-muted-foreground">
                                        <LoaderIcon className='animate-spin' /> <p>Thinking...</p>
                                    </div>
                                )}
                            </div>
                        </ScrollArea>

                        <form onSubmit={sendQuery} className="relative mt-2 p-8 w-full">
                            <div className="relative w-full">
                                <Textarea
                                    rows={2}
                                    className="pl-10 pr-10 py-2 w-full resize-none rounded-md border border-input bg-background text-sm shadow-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                                    placeholder="Ask something with AI"
                                    value={query}
                                    onChange={(e) => setQuery(e.target.value)}
                                    onKeyDown={(e) => {
                                        if (e.key === 'Enter' && !e.shiftKey) {
                                            e.preventDefault();
                                            sendQuery(e);
                                        }
                                    }}
                                />

                                {/* Send button (right) */}
                                <Button
                                    type="submit"
                                    variant="default"
                                    className="absolute right-2 bottom-2 w- p-0 rounded-sm"
                                >
                                    <SendHorizontalIcon className="h-12 w-12" />
                                </Button>
                            </div>
                        </form>
                    </div>
                </div>
            </Card>
        </div>
    );
}
