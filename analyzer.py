from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume.

    Give:
    1. Strengths
    2. Weaknesses
    3. ATS Improvement Suggestions
    4. Skills Improvement Suggestions

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional AI resume reviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content