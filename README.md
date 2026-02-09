📄 AI Document Generator Platform
Overview

The AI Document Generator Platform is an end-to-end application that generates professional documents such as resumes, letters, and contracts based on user prompts. The system processes user input through a backend API, leverages a large language model for content generation, stores outputs persistently, and enables real-time document retrieval.

Tech Stack

Backend: FastAPI (Python)

AI Model: Google Gemini API

Database: Azure Cosmos DB

Frontend: HTML / CSS / JavaScript (or React)

Cloud: Azure App Service

Document Formats: PDF, DOCX

Architecture & Data Flow
User Input (Frontend)
→ FastAPI Request Validation
→ Prompt Construction
→ Gemini API Inference
→ Document Formatting (PDF/DOCX)
→ Cosmos DB Storage
→ Real-time Retrieval & Download

Features

Schema-validated API for document generation

AI-powered content creation using Gemini

Persistent storage of user data and documents

Real-time retrieval of generated documents

Downloadable outputs in PDF and DOCX formats

Running the Project Locally
git clone <repo-url>
cd backend
pip install -r requirements.txt
python main.py


Create a .env file using .env.example and add required API keys.

Deployment

Backend deployed on Azure App Service

Environment variables managed via Azure configuration

Frontend hosted separately and connected via REST APIs
