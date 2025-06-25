import pdfplumber
import docx

def extract_text_from_file(file):
    try:
        file_path = file.name if hasattr(file, "name") else file

        if file_path.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        elif file_path.endswith(".docx"):
            doc = docx.Document(file_path)
            text = "\n".join(para.text for para in doc.paragraphs)
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            return " ❌ Error: Unsupported file format. Please upload a PDF, DOCX, or TXT file."
        
        if not text.strip():
            return " ⚠️ The file was empty or contained no extractable text."

        return text
    
    except Exception as e:
        return f"❌ An error occurred while reading the file: {str(e)}"