#  Advanced Prompt Engineering System

An interactive tool to perform NLP tasks using prompt-based generation and automatic evaluation. Built with Python and Streamlit, it supports:

-  Text Summarization  
-  Code Generation  
-  Data Extraction  
-  Question Answering  

---

##  Features

-  Modular file structure (`tasks/`, `utils/`)
-  Template-based prompt generation
-  Evaluation using ROUGE and BLEU scores
-  File upload support (PDF, DOCX, TXT, CSV)
-  Simple and clean Streamlit UI

---

##  How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Start the application

streamlit run streamlit_app.py

 Folder Structure
      
prompt-engineering/
│
├── tasks/
│   ├── summarization.py
│   ├── question_answering.py
│   ├── data_extraction.py
│   ├── code_generation.py
│   └── evaluation.py
│
├── utils/
│   ├── evaluate_scores.py
│   ├── extract_text.py
│   ├── metrics.py
│   └── templates.py
│
├── file_reader.py
├── prompt_generator.py
├── streamlit_app.py
├── requirements.txt
└── README.md


 Evaluation
This system uses the following metrics:

ROUGE: Measures similarity between generated and reference summaries

BLEU: Measures overlap between tokens in generated and reference answers
    

 Technologies Used
Python

Streamlit

NLTK – BLEU evaluation

ROUGE-Score – ROUGE-L evaluation

PyPDF2, docx, textract – File reading support