<p align="center">
  <img src="https://img.icons8.com/color/96/000000/document.png" alt="Docorator Logo" width="80" height="80">
  <h1 align="center">🪶 Docorator (Docgen)</h1>
  <p align="center">
    <strong>An AI-powered document generation platform that makes crafting professional documents effortless.</strong>
  </p>
  <p align="center">
    <a href="#features">Features</a> •
    <a href="#tech-stack">Tech Stack</a> •
    <a href="#getting-started">Getting Started</a> •
    <a href="#how-it-works">How It Works</a> •
    <a href="#license">License</a>
  </p>
</p>

---

## ✨ Overview

**Docorator** is a comprehensive document generation platform designed to help users quickly and accurately create high-quality documents such as Resumes, Statements of Purpose (SOPs), Formal Letters, Contracts, and Reports.

With Docorator, you can choose to enter your details manually or harness the power of **Google Gemini AI** to intelligently expand upon brief contexts and automatically fill in missing details, resulting in fully formatted `DOCX` and `PDF` files in seconds.

## 🚀 Features

- **Multi-Document Support**: Generate Resumes, SOPs, Formal Letters, Contracts, and Reports.
- **Two Generation Modes**:
  - ✍️ **Manual Mode**: Total control over the specific content of your document.
  - 🤖 **AI-Assisted Mode**: Provide basic context, and let Gemini AI draft professional content, expand on bullet points, and structure the data.
- **Instant Exports**: Download your finalized documents in both `DOCX` (Word) and `PDF` formats.
- **Secure Authentication**: Built-in user authentication (Sign Up / Log In) and secure password reset policies.
- **Document Dashboard**: A personal dashboard to track, view, and manage your previously generated documents.
- **Sleek UI/UX**: A responsive, modern frontend designed with intuitive user flows in mind.

## 🛠️ Tech Stack

**Frontend:**
- HTML5, CSS3, Vanilla JavaScript
- Google Fonts (Outfit) & FontAwesome Icons

**Backend:**
- **Python / FastAPI**: High-performance backend routing and API management.
- **Uvicorn & Gunicorn**: Robust production-ready ASGI servers.
- **Google Gemini API**: Advanced LLM integration for AI-driven document drafting.
- **python-docx / docxtpl**: Template rendering and DOCX generation.
- **LibreOffice**: Headless conversion of DOCX files to PDF.
- **Azure Cosmos DB**: Highly scalable NoSQL database for managing users and document metadata.
- **Docker**: Containerized deployment for consistent environments.

## 📂 Project Structure

```text
Docgenerator/
├── backend/
│   ├── main.py                 # FastAPI application and route handlers
│   ├── auth.py                 # JWT authentication and password hashing
│   ├── database.py             # Azure Cosmos DB connection logic
│   ├── models.py               # Data models for Users and Documents
│   ├── ai_client.py            # Integration with Google Gemini API
│   ├── template_renderer.py    # DOCX rendering and PDF conversion logic
│   ├── Dockerfile              # Docker configuration for backend
│   └── templates/              # Base DOCX templates for different document types
├── frontend/
│   ├── index.html              # Main document generation interface
│   ├── dashboard.html          # User document dashboard
│   ├── profile.html            # User profile management
│   ├── app.js                  # Core frontend logic
│   ├── auth.js                 # Frontend authentication handling
│   └── style.css               # Application styling
└── data/                       # Persistent storage map
```

## 🏃 Getting Started

### Prerequisites

Ensure you have the following installed on your machine:
- **Python 3.10+**
- **Docker** (optional, but recommended for consistent environments)
- **Node.js / Live Server** (optional, for running the frontend locally)
- A **Google Gemini API Key**
- An **Azure Cosmos DB** instance

### Local Setup (Without Docker)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ananjay07/Docgen.git
   cd Docgen/backend
   ```

2. **Set up the virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: You will also need LibreOffice installed on your system for PDF conversion).*

4. **Environment Variables:**
   Create a `.env` file in the `backend/` directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   COSMOS_DB_URI=your_cosmos_db_uri
   COSMOS_DB_KEY=your_cosmos_db_key
   SECRET_KEY=your_jwt_secret_key
   # STORAGE_DIR=../data (Optional)
   ```

5. **Run the Backend:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

6. **Run the Frontend:**
   Serve the `frontend/` directory using any static file server, such as Live Server in VS Code, or Python's HTTP server:
   ```bash
   cd ../frontend
   python -m http.server 3000
   ```
   Open `http://localhost:3000` in your browser.

### Running with Docker

1. **Build the container:**
   ```bash
   cd backend
   docker build -t docorator-backend .
   ```

2. **Run the container:**
   Make sure to pass your `.env` variables or mount a volume if necessary.
   ```bash
   docker run -d -p 8000:8000 --env-file .env docorator-backend
   ```

## 🧠 How the AI works

When using **AI Assisted Mode**, the frontend collects your basic form inputs along with a specific "AI Context" (e.g., "Emphasize my leadership skills and keep the tone strictly formal"). The backend forwards this context to **Google Gemini**, which intelligently constructs a structured JSON response tailored to the document type (e.g., separating an SOP into Background, Motivation, and Future Goals). This structured data is then instantly mapped to the underlying DOCX template.


## 📄 License

This project is open-source and available under standard open source licensing.
