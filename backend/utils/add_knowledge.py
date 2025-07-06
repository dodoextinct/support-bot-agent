from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.mongodb import MongoDb
from pathlib import Path
import os
from agno.knowledge.combined import CombinedKnowledgeBase
from dotenv import load_dotenv

from agno.knowledge.docx import DocxKnowledgeBase

mongo_url = os.getenv("MONGO_DB_URL")

vector_db = MongoDb(
    collection_name="support_docs", db_url=mongo_url, search_index_name="support_index"
)

doc_kb = DocxKnowledgeBase(
    path=Path("knowledge/docs"),
    vector_db=vector_db,
)

# Markdown Knowledge Base
markdown_kb = MarkdownKnowledgeBase(
    path=Path("knowledge/markdown"),
    vector_db=vector_db,
)

# PDF Knowledge Base
pdf_kb = PDFKnowledgeBase(
    path=Path("knowledge/pdfs"),
    reader=PDFReader(chunk=True),
    vector_db=vector_db,
)

# One-time loading to vector DB
markdown_kb.load(recreate=False)
pdf_kb.load(recreate=False)
doc_kb.load(recreate=False)
# Combined knowledge base for agent

combined_knowledge_base = CombinedKnowledgeBase(
    sources=[
        doc_kb,
        markdown_kb,
        pdf_kb,
    ],
    vector_db=vector_db
)

print("Knowledge ingested.")
