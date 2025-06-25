import os
import textract
import csv
import docx
import PyPDF2


def extract_text(file):
    """
    Extract text from uploaded file (PDF, DOCX, TXT, CSV).
    """
    file_path = file.name if hasattr(file, "name") else file
    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".pdf":
            return extract_from_pdf(file)
        elif ext == ".docx":
            return extract_from_docx(file)
        elif ext == ".txt":
            return extract_from_txt(file)
        elif ext == ".csv":
            return extract_from_csv(file)
        else:
            # Fallback to textract
            return textract.process(file_path).decode("utf-8")
    except Exception as e:
        return f" ❌ Failed to extract text: {str(e)}"


def extract_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_from_txt(file):
    return file.read().decode("utf-8", errors="ignore")


def extract_from_csv(file):
    decoded = file.read().decode("utf-8", errors="ignore").splitlines()
    reader = csv.reader(decoded)
    return "\n".join([", ".join(row) for row in reader])