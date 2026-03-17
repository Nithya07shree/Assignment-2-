# importing required libraries 
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("API key not found. Please check your environment var file.")
    exit(1)
client = Groq(api_key=GROQ_API_KEY)

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

def query_model(user_prompt: str) -> str | None:
    """
    query the model with user's prompt

    Args:
        user_prompt (str): user's prompt text

    Returns:
        str | None: model's response text
    """
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model = "llama-3.1-8b-instant",
            temperature=0.4,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main() -> None:
    """accepts user prompt and query the model
    """
    try:
        print("Querying Llama-3.1 ...")
        prompt: str = input("Enter your query: ")
        result= query_model(prompt)
        print("Response: ")
        print(result)
    except Exception as e:
        print(f"Exception occured: {e}")

if __name__ == "__main__":
    main()