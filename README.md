# AutoStream AI Agent 🤖

This project is a conversational AI agent built for the ServiceHive Internship Assignment. It simulates an AI-powered SaaS assistant that converts user conversations into qualified leads through intelligent intent detection and a guided workflow.

---

## 🚀 Features

- **Intent Detection:** Categorizes user input (greeting, pricing, high-intent) using structured LLM prompting.
- **RAG-based Knowledge Retrieval:** Uses a local JSON-based knowledge base for accurate, context-aware responses.
- **Lead Capture Workflow:** Automatically triggers lead collection (name, email, platform) when high intent is detected.
- **Multi-turn Memory:** Maintains conversation state to ensure a smooth transition from inquiry to lead capture.
- **Modern UI:** A clean, ChatGPT-style interface for a seamless user experience.

---

## 🧠 Architecture

This project uses a modular agent-based design.

The system integrates an LLM for reasoning and natural conversation. A local JSON-based knowledge base is used for Retrieval-Augmented Generation (RAG), ensuring accurate responses.

Intent detection is handled via structured LLM prompting, returning both intent and response in JSON format. This enables clean separation of reasoning and execution.

State is managed using an in-memory dictionary that tracks conversation flow across multiple turns, allowing the agent to transition into lead collection mode only when high intent is detected.

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **AI/LLM:** OpenAI GPT / LangChain
- **Frontend:** HTML, CSS, JavaScript
- **Data:** JSON

---

## 📂 Project Structure

```text
autostream-ai-agent/
├── api.py              # Backend Logic
├── knowledge.json      # RAG Data
├── requirements.txt    # Dependencies
└── static/             # Frontend Files
```

##⚙️ How to Run
1. Clone the repository
git clone <your-repo-link>
cd autostream-ai-agent

2. Create and Activate Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
python -m uvicorn api:app --reload

5. Open in browser
Visit: http://127.0.0.1:8000/

## 🖼️ Demo UI
[AutoStream Demo](assets/screenshot.png)

👤 Author
Atharva Manoj Shivade

CSE AI & ML Student
