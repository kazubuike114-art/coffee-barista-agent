import os
from google import genai

def root_agent(prompt, api_key=None):
    # Use the passed API key or fallback to environment variables
    key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text
    
