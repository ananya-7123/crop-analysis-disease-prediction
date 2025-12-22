# crop-analysis-disease-prediction
Multimodal Crop Disease and Suitability Prediction using ML and NLP

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)
![React](https://img.shields.io/badge/React-18+-61DAFB.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

</div>

## 📸 **Screenshots**

### Crop Prediction Interface
![Crop Prediction](docs/images/crop-prediction-demo.png)

### Disease Detection Dashboard
![Disease Detection](docs/images/disease-detection-demo.png)

### Integrated Advisory Report
![Advisory Report](docs/images/advisory-report-demo.png)

*Screenshots coming soon as development progresses*

## ⚡ **Quick Start**
```bash
# Clone the repository
git clone https://github.com/ananya-7123/crop-analysis-disease-prediction.git
cd crop-analysis-disease-prediction

# Frontend
cd frontend && npm install && npm start

# Backend (new terminal)
cd backend && npm install && npm start

# ML Pipeline (new terminal)
cd ml-pipeline-crop && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

**📖 For detailed setup instructions, see [Setup Guide](docs/setup-guide.md)**

## 📡 **API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/crop/predict` | Predict suitable crop |
| POST | `/api/disease/analyze` | Analyze disease from text |
| GET | `/api/models/status` | Check model availability |

**Full API documentation:** [API Docs](docs/api-docs.md)

## 🔄 **System Workflow**
```mermaid
graph LR
    A[User Input] --> B{Input Type}
    B -->|Soil Data| C[Crop Prediction ML]
    B -->|Text Report| D[Disease Detection NLP]
    C --> E[Advisory Report]
    D --> E
    E --> F[Display Results]
```

## 📂 **Project Structure**
```
crop-analysis-disease-prediction/
├── frontend/                 # React UI
├── backend/                  # Express API
├── ml-pipeline-crop/         # Crop prediction models
├── nlp-pipeline-disease/     # Disease detection NLP
├── datasets/                 # Dataset references only
│   ├── structured/           # Crop data sources
│   └── unstructured/         # Text data sources
├── docs/                     
│   ├── setup-guide.md        # Detailed setup instructions
│   ├── api-docs.md           # API documentation
│   └── images/               # Screenshots
└── README.md
```

⚠️ **Raw datasets and trained models are NOT committed to Git**

## ⚠️ **Important Notes**

### **What NOT to Commit:**
- ❌ Raw datasets (`datasets/*`)
- ❌ Trained model files (`.pkl`, `.joblib`, `.h5`)
- ❌ Environment files (`.env`)
- ❌ `node_modules/` or `venv/`

### **Dataset Access:**
- All datasets are publicly available (see [Datasets](#-datasets))
- Download instructions in `datasets/README.md`
- Store locally in respective folders after download

### **Model Files:**
- Train models locally using provided scripts
- Models auto-save to `ml-pipeline-crop/models/` and `nlp-pipeline-disease/models/`

## 🔧 **Troubleshooting**

| Issue | Solution |
|-------|----------|
| Port already in use | Change port in `.env` file |
| Module not found | Run `pip install -r requirements.txt` again |
| Models not loading | Run training scripts in ML pipeline folders |
| CORS errors | Check backend CORS configuration |

**For more help, see [Setup Guide](docs/setup-guide.md) or open an issue**

## 🗺️ **Roadmap**

### Phase 1: MVP Development ✅
- [x] Project setup and architecture
- [x] Dataset collection
- [x] Basic ML pipeline
- [ ] NLP pipeline completion
- [ ] Frontend-backend integration

### Phase 2: Enhancement 🔄
- [ ] Model optimization
- [ ] UI/UX improvements
- [ ] Performance testing
- [ ] Documentation completion

### Phase 3: Deployment 📦
- [ ] Cloud deployment
- [ ] CI/CD pipeline
- [ ] Monitoring setup

## 🙏 **Acknowledgments**

- **Datasets:** Kaggle, UCI ML Repository, Government of India
- **Inspiration:** Agricultural technology research papers
- **Tools:** scikit-learn, NLTK, React, Express.js
- **Mentor/Guide:** [If applicable]
- [ ] User testing

