import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import streamlit as st

# Get the OpenAI API key
_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("📝 File Q&A (Supporting TXT and MD)")
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question:
    article = uploaded_file.read().decode()
    client = OpenAI(api_key=openai_api_key)
    assistant = client.beta.assistants.create(
        name="Financial Analyst Assistant",
        instructions="You are an expert financial analyst. Use you knowledge base to answer questions about audited financial statements.",
        model="gpt-4o-mini",
        tools=[{"type": "file_search"}],
        )
    
    # Create a vector store caled "Financial Statements"
    vector_store = client.beta.vector_stores.create(name="Financial Statements")
    # Ready the files for upload to OpenAI
    file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"]
    file_streams = [open(path, "rb") for path in file_paths]
 
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
        )
 
    # You can print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)