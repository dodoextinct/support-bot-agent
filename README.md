-----

# Support Bot Agent – Full Stack Application

A full-stack AI-powered chatbot that answers user queries based on your custom knowledge base. This application combines OpenAI's language model with vector search capabilities for markdown, PDF, and various document file types.

-----

## Features

  * **AI-powered support assistant**: Get intelligent answers to your questions.
  * **Contextual retrieval**: The chatbot retrieves relevant information from your uploaded documents (PDFs, Markdown, etc.).
  * **Clean Tailwind UI**: Enjoy a modern and responsive user interface with real-time chat.
  * **Markdown-formatted answers**: Responses are rendered beautifully with Markdown.
  * **Handles follow-up messages**: Engage in natural, multi-turn conversations.
  * **Dockerized for easy deployment**: Deploy your chatbot effortlessly using Docker.

-----

## Tech Stack

### Backend

  * **Python**: The core logic is built with Python.
  * **Flask**: A lightweight web framework for the API.
  * **Agno SDK**: Used for building AI workflows and agents.
  * **MongoDB**: The primary database, with Atlas Vector Search for efficient retrieval.
  * **PDF/Markdown parsers**: For ingesting knowledge from various file types.

### Frontend

  * **Next.js (App Router)**: A React framework for building the user interface.
  * **Tailwind CSS**: For rapid and consistent UI styling.
  * **marked.js**: For rendering Markdown content.

### Other

  * **Vector Store**: MongoDB Atlas Search
  * **LLM**: OpenAI GPT-4o
  * **Containerization**: Docker + Docker Compose

-----

## Project Structure

```
.
├── backend/
│ ├── main.py # Flask app entrypoint
│ ├── routes/ # API endpoints
│ ├── workflows/ # Workflow logic invoking agents
│ ├── user_agents/ # Agent creation using Agno
│ ├── utils/ # Knowledge ingestion from files
│ ├── requirements.txt
│ └── ee.env.example # Environment variable template
├── frontend/
│ ├── app/ # Next.js app directory
│ ├── components/ # Chatbot UI components
│ ├── public/ # Static files
│ ├── out/ # Output after export
│ └── package.json
├── docker-compose.yml
├── Dockerfile (in both frontend and backend directories)
```

-----

## Getting Started

Follow these steps to get your AI Support Chatbot up and running.

### 1\. Clone the repository

```bash
git clone https://github.com/your-username/ai-support-chatbot.git
cd support-bot-agent
```

### 2\. Set up Environment Variables

Rename the provided `.env` template file:

```bash
cp env.local.frontend.example frontend/.env.local
cp env.backend.example backend/.env
```

Now, open `backend/.env` and add your secrets:

```env
OPENAI_API_KEY=your_openai_key
MONGO_DB_URL=your_mongodb_connection_string
```

** Secrets Required:**
You'll need the following:

  * **`OPENAI_API_KEY`**: Your API key from OpenAI (used for chat/completions).
  * **`MONGO_DB_URL`**: Your MongoDB Atlas connection string (used for the vector database).

### 3\. Run with Docker Compose (Recommended)

Build and start the frontend and backend services together:

```bash
docker compose up --build
```

Once started, you can access:

  * **Frontend**: `http://localhost:3000`
  * **Backend API**: `http://localhost:8000/support`

### 4\. Manual Run (Alternative to Docker)

#### Backend

```bash
cd backend
pip install -r requirements.txt
python main.py
```

#### Frontend

```bash
cd frontend
npm install
npm run build
npx run dev
```

-----

## Notes

  * Ensure that **MongoDB Atlas vector search** and **OpenAI API access** are properly set up with your provided keys.

-----

## 💡 To-Do / Ideas

  * Add support for file uploads via the frontend.
  * Stream AI response rendering for a more dynamic user experience.

-----

Build by Yash Krishan
