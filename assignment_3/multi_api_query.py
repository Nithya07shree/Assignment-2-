import streamlit as st
import time

# import functions for AI responses
from cohere_example import query_model_cohere
from gemini_example import query_model_gemini
from groq_example import query_model_groq
from huggingface_example import query_model_hf
from ollama_example import query_model_ollama

# HELPER FUNCTIONS
# map model names to functions
MODEL_MAPPING = {
    "cohere/command-r7b-12-2024" : query_model_cohere,
    "gemini-3-flash-preview" : query_model_gemini,
    "groq/Llama-3.1" : query_model_groq,
    "hf/Mistral-7B-Instruct-v0.2" : query_model_hf,
    "ollama/qwen2.5-coder" : query_model_ollama
}

# simulate streaming as functions return plain/static strings
def stream_response(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.01)


# STREAMLIT UI 

st.title("TALK TO YOUR BOT")

# Sidebar for selecting model 
with st.sidebar:
    selected_model = st.selectbox(
        "Choose your LLM",
        options=list(MODEL_MAPPING.keys()),
        key="model_choice"
    )
    st.info(f"Currently chatting with: **{selected_model}**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's up?"):
    
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display assistant response in chat message container
    # write_stream is used to write response with a typewriter effect
    with st.chat_message("assistant"):
        # call the function based on selection
        model_function = MODEL_MAPPING[st.session_state.model_choice]
        model_response = model_function(prompt)
        # stream the result
        response = st.write_stream(stream_response(model_response))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})