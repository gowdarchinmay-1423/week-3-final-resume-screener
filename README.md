# Resume-Screening-App
Resume Screening App With Python and Machine Learning 
Optional: Place your ML model files (clf.pkl, tfidf.pkl, encoder.pkl) in the same folder for predictions.

# Resume Screener - Week 3 (Final Project)

## Overview
This is the **final project** version of the Resume Screener.  
- Includes all features from Week 1 & 2  
- Modularized code for better readability  
- Streamlit interface improvements  
- Placeholder predictions since large ML model files are not included in GitHub  

**Note:** To run actual predictions, download the `.pkl` model files locally.

## Features
- Upload PDF, DOCX, TXT resumes
- Extract and clean resume text
- Display extracted text
- Show predicted category (placeholder in GitHub version)

## Files
- `app.py` – Main Streamlit app
- `README.md` – Project description
- `reqiurements.txt` – Required Python packages
- `.gitignore` – To ignore large `.pkl` files

## How to Run
1. Install dependencies:
   ```bash
   Run the Streamlit app:

streamlit run app.py
Optional: Place ML model files (clf.pkl, tfidf.pkl, encoder.pkl) locally to get actual predictions.

   pip install -r reqiurements.txt

