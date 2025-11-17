import streamlit as st
import re
import docx
import PyPDF2
import os

# Base folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dummy placeholders instead of large ML files
svc_model = None
tfidf = None
le = None

# Function to clean resume text
def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)
    cleanText = re.sub(r'RT|cc', ' ', cleanText)
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)
    cleanText = re.sub(r'@\S+', '  ', cleanText)
    cleanText = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub(r'\s+', ' ', cleanText)
    return cleanText

# Extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Extract text from TXT
def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text

# Handle uploaded file
def handle_file_upload(uploaded_file):
    ext = uploaded_file.name.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif ext == 'docx':
        return extract_text_from_docx(uploaded_file)
    elif ext == 'txt':
        return extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Upload PDF, DOCX, or TXT.")

# Dummy prediction
def pred(input_resume):
    # Placeholder since ML model is removed
    return "Model not deployed - large files excluded from GitHub"

# Streamlit app
def main():
    st.set_page_config(page_title="Resume Category Prediction - Week 3", layout="wide")
    st.title("Resume Category Prediction - Week 3")
    st.markdown("Upload a resume (PDF, DOCX, TXT) to predict the job category using ML.")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf","docx","txt"])
    if uploaded_file:
        try:
            resume_text = handle_file_upload(uploaded_file)
            st.success("Text successfully extracted from resume!")
            
            if st.checkbox("Show extracted text", False):
                st.text_area("Extracted Resume Text", resume_text, height=300)

            st.subheader("Predicted Category")
            category = pred(resume_text)
            st.write(f"**{category}**")
        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")

if __name__ == "__main__":
    main()
