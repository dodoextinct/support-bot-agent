"use client";

import { Chatbot } from "@/components/blocks/chatbot";
import { ScrollArea } from "@/components/ui/scroll-area";
import { HammerIcon } from "lucide-react";
import React from "react";

export default function Home() {
  return (
    <ScrollArea className="flex justify-between bg-gray-100 min-h-screen text-foreground p-4">
      <Chatbot />
      <div className="flex items-center space-x-2 w-full justify-center italic text-xs mt-10">
        <HammerIcon /> <p>Build by Yash Krishan</p>
      </div>
    </ScrollArea>
  );
}
