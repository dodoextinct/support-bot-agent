from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.mongodb import MongoMemoryDb
from agno.storage.mongodb import MongoDbStorage
from utils.add_knowledge import combined_knowledge_base
import os
from textwrap import dedent
from agno.models.groq import Groq


def get_support_agent(session_id="support-session"):
    mongo_url = os.getenv("MONGO_DB_URL")
    mongo_db_name = os.getenv("MEMORIES_DB")
    collection_name = "support_agent"

    memory = Memory(
        db=MongoMemoryDb(
            collection_name=f"{collection_name}_memory",
            db_url=mongo_url,
            db_name=mongo_db_name,
        ),
        model=OpenAIChat(id="gpt-4o"),
    )

    storage = MongoDbStorage(
        collection_name=f"{collection_name}_chat",
        db_url=mongo_url,
        db_name=mongo_db_name,
    )

    return Agent(
        name=collection_name,
        session_id=session_id,
        model=OpenAIChat(id="gpt-4o", max_retries=1),
        memory=memory,
        storage=storage,
        enable_agentic_memory=True,
        enable_user_memories=True,
        read_chat_history=True,
        add_history_to_messages=True,
        num_history_runs=3,
        tools=[],
        show_tool_calls=False,
        markdown=True,
        debug_mode=True,
        retries=1,
        delay_between_retries=1,
        exponential_backoff=False,
        knowledge=combined_knowledge_base,
        search_knowledge=True,
        description=dedent(
            """
            You are a helpful support assistant for Angel One customers.

            You only answer questions based on the provided knowledge base,
            which includes Angel One documentation and insurance PDFs.
        """
        ),
        instructions=[
            "If the answer is not in the knowledge base, respond with: 'I don't know.'",
            "Always answer only 'I don't know' if answer is not present in knowledge base, never make answers on own",
            "Do not hallucinate or assume answers.",
            "Do not include disclaimers.",
            "Respond clearly and concisely using markdown.",
            "Format your answers beautifully using markdown."
        ],
    )
