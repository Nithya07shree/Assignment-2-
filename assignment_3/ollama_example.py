# importing required libraries 
from ollama import chat

# Defines the AI's role, output structure, response tone and behavioral constraints
SYSTEM_PROMPT = """ You are a helpful AI assistant. Your goal is to provide accurate, factual, and actionable answers to the user's question.
Requirements:
- Analyze the task and break it into small logical steps; plan before answering.
- Keep explanations concise; prefer bullet points or a structured format.
- Maintain a professional, polite tone.
- If you are unsure, say so instead of making things up.
Constraints:
- Avoid complex jargon unless the user requests it.
- Do not provide harmful or unethical content.
"""

def query_model_ollama(user_prompt: str) -> str | None:
    """
    query the model with user's prompt

    Args:
        user_prompt (str): user's prompt text

    Returns:
        str | None: model's response text
    """
    try:
        response = chat(
            model='qwen2.5-coder:3b',
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    'role':'user',
                    'content':user_prompt,
                }
        ])
        return response.message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
def main() -> None:
    """accepts user prompt and query the model
    """
    try:
        print("Querying qwen2.5-coder ...")
        prompt: str = input("Enter your query: ")
        result= query_model_ollama(prompt)
        print("Response: ")
        print(result)
    except Exception as e:
        print(f"Exception occured: {e}")

if __name__ == "__main__":
    main()