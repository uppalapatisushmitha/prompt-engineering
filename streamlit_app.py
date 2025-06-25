# streamlit_app.py

import streamlit as st
from tasks.summarization import summarize_text
from tasks.code_generation import generate_code
from tasks.data_extraction import extract_full_text, extract_answer_from_text
from tasks.evaluation import evaluate_rouge_bleu
from file_reader import extract_text

#
st.set_page_config(page_title="Advanced Prompt Engineering", layout="wide")
st.markdown("""
    <style>
        code {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
        }
        textarea {
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'> Advanced Prompt Engineering</h1>
    <hr style='border:1px solid #ddd;'>
""", unsafe_allow_html=True)

# --------------------- Sidebar Task Selection ---------------------
with st.sidebar:
    st.header(" Select Task")
    task = st.selectbox("Choose a Task", [
        "summarization", "code generation", "data extraction", "question answering"
    ])


if task == "summarization":
    st.header("📄 Text Summarization")
    input_text = st.text_area(" Enter Text to Summarize", height=200)
    output_container = st.container()

    if st.button(" Run Summarization", key="summarize_button") and input_text:
        system_prompt = "Act as a skilled assistant. Provide a short, insightful summary that highlights the main ideas clearly and succinctly."
        full_prompt = f"{system_prompt}\n\nSummarize the following text:\n{input_text}"

        summary = summarize_text(input_text)
        rouge, bleu = evaluate_rouge_bleu(input_text, summary)

        with output_container:
            st.markdown("###  System Prompt")
            st.code(system_prompt, language="text")

            st.markdown("###  Full Prompt")
            st.code(full_prompt, language="text")

            st.markdown("###  Output Summary")
            st.text_area("Summary", summary, height=200)

            st.markdown("###  Evaluation")
            st.success(f"ROUGE-L: {rouge} | BLEU: {bleu}")


elif task == "code generation":
    st.header("💻 Code Generation")
    prompt = st.text_area(" Enter your prompt", height=150)
    language = st.selectbox(" Select Language", ["Select Language", "Python", "Java", "C++", "JavaScript", "HTML"])

    if language != "Select Language":
        if st.button(" Run Code Generation", key="code_gen_button") and prompt:
            system_prompt = "Act as a helpful code generator. Based on the input prompt and selected language, generate clean and functional code."
            full_prompt = f"{system_prompt}\n\nLanguage: {language}\nPrompt: {prompt}"

            code = generate_code(prompt, language)
            rouge, bleu = evaluate_rouge_bleu(prompt, code)

            st.markdown("###  System Prompt")
            st.code(system_prompt, language="text")

            st.markdown("###  Full Prompt")
            st.code(full_prompt, language="text")

            st.markdown("###  Generated Code")
            st.text_area("Code", code, height=200)

            st.markdown("###  Evaluation")
            st.success(f"ROUGE-L: {rouge} | BLEU: {bleu}")
    elif st.button(" Run Code Generation", key="code_gen_warning"):
        st.warning("Please select a language before generating code.")


elif task == "data extraction":
    st.header("📂 Data Extraction from File")

    if "raw_text" not in st.session_state:
        st.session_state.raw_text = None
        st.session_state.data_file_uploaded = False

    uploaded_file = st.file_uploader("📎 Upload File", type=["pdf", "docx", "txt", "csv"])

    if uploaded_file:
        if st.button(" Run Data Extraction", key="extract_button"):
            raw_text = extract_full_text(uploaded_file)
            if raw_text.startswith("❌") or raw_text.startswith("⚠️"):
                st.error(raw_text)
                st.session_state.raw_text = None
                st.session_state.data_file_uploaded = False
            else:
                st.session_state.raw_text = raw_text
                st.session_state.data_file_uploaded = True

    if st.session_state.data_file_uploaded and st.session_state.raw_text:
        st.markdown("###  Extracted Content")
        st.text_area("File Content", st.session_state.raw_text, height=250)

        st.markdown("###  Ask a Question About the File")
        question = st.text_input("Enter your question")

        if question:
            if st.button(" Get Answer", key="extract_answer"):
                answer = extract_answer_from_text(st.session_state.raw_text, question)
                rouge, bleu = evaluate_rouge_bleu(question, answer)

                st.markdown("###  Answer")
                st.text_area("Answer", answer, height=100)

                st.markdown("###  Evaluation")
                st.success(f"ROUGE-L: {rouge} | BLEU: {bleu}")


elif task == "question answering":
    st.header("❓ File-Based Question Answering")

    if "qa_task_active" not in st.session_state or not st.session_state.qa_task_active:
        st.session_state.qa_text = None
        st.session_state.qa_uploaded = False
        st.session_state.qa_file = None
        st.session_state.qa_task_active = True

    uploaded_file = st.file_uploader("📎 Upload File", type=["pdf", "docx", "txt", "csv"])

    if uploaded_file and uploaded_file != st.session_state.get("qa_file"):
        st.session_state.qa_file = uploaded_file
        raw_text = extract_full_text(uploaded_file)
        if raw_text.startswith("❌") or raw_text.startswith("⚠️"):
            st.error(raw_text)
            st.session_state.qa_text = None
            st.session_state.qa_uploaded = False
        else:
            st.session_state.qa_text = raw_text
            st.session_state.qa_uploaded = True

    if st.session_state.qa_uploaded and st.session_state.qa_text:
        question = st.text_input(" Ask a question about the file")

        if question and st.button(" Get Answer", key="qa_button"):
            answer = extract_answer_from_text(st.session_state.qa_text, question)
            rouge, bleu = evaluate_rouge_bleu(question, answer)

            st.markdown("###  Answer")
            st.text_area("Answer", answer, height=100)
            st.markdown("###  Evaluation")
            st.success(f"ROUGE-L: {rouge} | BLEU: {bleu}")

