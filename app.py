import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import streamlit as st

# Get the OpenAI API key
_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")
    
client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)