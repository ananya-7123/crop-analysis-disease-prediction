# 🛠️ Project Setup Guide

This guide explains how to set up and run the **Multimodal Crop Health & Suitability Prediction** project locally.

It is intended for **team members, reviewers, and evaluators** to easily understand and run different parts of the system.

---

## 📌 Project Overview

This project is a **multimodal machine learning–based agricultural decision support system** that integrates:

- **Structured soil–climate data** → Crop suitability prediction
- **Unstructured farmer/drone text reports** → Disease risk detection

The system is built as a **full-stack application** with ML pipelines integrated into the backend.

---

## 📂 Repository Structure

Top-level folders and purpose:

- `frontend/` — React web app (UI)
- `backend/` — Node.js + Express API
- `ml-pipeline-crop/` — Crop suitability ML pipeline
- `nlp-pipeline-disease/` — Disease detection NLP pipeline
- `datasets/` — Dataset references (do not commit raw data)
- `docs/` — Project documentation

```text
crop-analysis-disease-prediction/
├── frontend/                 # React frontend
├── backend/                  # Node.js + Express backend
├── ml-pipeline-crop/         # Crop suitability ML pipeline
├── nlp-pipeline-disease/     # Disease detection NLP pipeline
├── datasets/                 # Dataset references (no actual data)
│   ├── structured/
│   └── unstructured/
├── docs/                     # Documentation
│   ├── setup-guide.md
│   └── api-docs.md
└── README.md
```

⚠️ **Note:** Actual datasets and trained model files are NOT pushed to GitHub.

---

## 🧰 Prerequisites

Ensure the following tools are installed on your system:

### 🔹 Common

- Git
- VS Code (recommended)

### 🔹 Frontend

- Node.js (v18+ recommended)
- npm or yarn

### 🔹 Backend

- Node.js
- npm

### 🔹 Machine Learning / NLP

- Python 3.9+
- pip
- Virtual environment tool (`venv` or `conda`)

---

## 🔽 Setup Steps

### 🔽 Step 1: Clone the Repository

```bash
git clone https://github.com/ananya-7123/crop-analysis-disease-prediction.git
cd crop-analysis-disease-prediction
```

### 🖥️ Step 2: Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

Frontend will run at: http://localhost:3000

This provides the user interface for inputs and predictions

### 🧠 Step 3: Backend Setup (Node.js + Express)

```bash
cd backend
npm install
npm start
```

Backend will run at: http://localhost:5000 (default)

Provides REST APIs for:

Crop prediction

Disease detection

Integration logic

📌 Environment variables (e.g., DB URI) should be added via a .env file (not committed).

### 🤖 Step 4: ML Pipeline Setup (Crop Suitability)

```bash
cd ml-pipeline-crop
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python train.py
```

Trains crop suitability models

Saves trained models locally (ignored by Git)

### 📝 Step 5: NLP Pipeline Setup (Disease Detection)

```bash
cd nlp-pipeline-disease
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python train.py
```

Trains NLP models using text data

Uses TF-IDF + classical ML models

### 🔗 Step 6: Backend ↔ ML Integration

- Backend invokes ML/NLP scripts or services for predictions.
- Trained models are loaded dynamically (local files or model server).
- API contracts for prediction endpoints are documented in `docs/api-docs.md`.

### 📊 Dataset Handling (Important)

- **Do NOT** upload raw datasets or trained model files to GitHub.
- Only store dataset sources, descriptions, and data access instructions in the repo.
- Refer to `docs/decisions-and-docs.md` (Notion) for dataset links and access procedures.

### 👥 Team Collaboration Rules

- Always run `git pull origin main` before starting work.
- Commit only working code with descriptive commit messages.
- Do **not** commit:
  - `datasets/`
  - `.env` files
  - Trained model files (e.g., `.pkl`, `.joblib`)
- Use Notion for:
  - workflow
  - task tracking
  - decisions

### 🚀 Deployment (Later Phase)

- Frontend: Vercel / Netlify
- Backend: Render / Railway
- ML services: containerized or served separately (optional)

### 🧪 Troubleshooting

- If dependency installation fails → recheck Node/Python versions and package manager.
- If ports clash → update port numbers in config and restart services.
- If models are missing → retrain locally or verify model storage path.
---
### 📌 Final Notes

This project is a college mini-project and follows clean engineering practices, documentation standards, and collaborative workflows.

For any issues, refer to:

- `README.md`
- `docs/api-docs.md`
- Project Notion workspace

---
