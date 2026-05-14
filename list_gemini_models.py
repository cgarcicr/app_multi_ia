import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "<TU_API_KEY_AQUI>")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={GEMINI_API_KEY}"

response = requests.get(url)
print(response.json())
