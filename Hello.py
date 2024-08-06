import streamlit as st

st.set_page_config(
    page_title="Dita's Home LLM",
    page_icon="🏠",
)

st.write("# Dita's Home LLM 🏠")

st.sidebar.success("Select a service above.")

st.markdown(
    """
    This is the Home of Dita's personal and local use of various LLM.
    Some are proprietary (OpenAI) and some are open-source through Ollama.
    **👈 Select a service from the sidebar**
    """
)
