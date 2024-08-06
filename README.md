# Chat with LLMs with Streamlit

Learning to use Streamlit, based on the LLM example uses provided in the references (with slight tweaks). Please update `system` prompt **in the code** for better experience. Easier UI for system prompt is upcoming.
1. GPT-4o Mini Chatbot `1_🤖_OpenAI_Chatbot.py`
2. Open-Source LLM Chatbot using Ollama `2_🦙_Ollama_Chatbot.py` (LLM: Gemma 2 9B, Llama 3.1 8B, Mistral 7B) **local**

## Preparation
1. Prepare OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys). This can be obtained by registering an OpenAI account (the one you use for ChatGPT works) and put some credit into your account (by registering your credit card). You will be charged as you go.
2. Install Ollama in your PC, please read [Ollama Documentation](https://github.com/ollama/ollama).
3. Download open-source LLMs into your PC, in this case `gemma2`, `llama3.1`, and `mistral` with `ollama pull <llm-name>` command. [Ollama Documentation](https://github.com/ollama/ollama)

## How to Run
### Clone the repository
Project repo:
```bash
https://github.com/RiaAyuP/streamlitchat1
```
### Create a conda environment after opening the repository
```bash
conda create -p env python=3.10 -y
```
```bash
conda activate env
```

### Install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your OpenAI credentials as follows:
```bash
OPENAI_API_KEY = "YOUR OPENAI KEY"
```

### Run the chatbot application
```bash
streamlit run Hello.py
```

## References
1. [Streamlit LLM Examples](https://llm-examples.streamlit.app/)
2. [Ollama Documentation](https://github.com/ollama/ollama)