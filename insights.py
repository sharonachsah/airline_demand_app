import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_insights(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are an airline market demand analyst."},
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message.content.strip()
