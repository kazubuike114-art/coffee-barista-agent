import os
from google import genai

def root_agent(prompt):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text
