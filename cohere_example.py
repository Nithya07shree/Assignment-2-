# importing required libraries 
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY: str | None = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    print("API key not found. Please check your environment var file.")
    exit(1)
client = cohere.ClientV2(COHERE_API_KEY)

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
        response = client.chat(
            model="command-r7b-12-2024",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ]
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"
    
def main() -> None:
    """accepts user prompt and query the model
    """
    try:
        print("Querying command-r7b-12-2024")
        prompt: str = input("Enter your query: ")
        result= query_model(prompt)
        print("Response: ")
        print(result)
    except Exception as e:
        print(f"Exception occured: {e}")

if __name__ == "__main__":
    main()