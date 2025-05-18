import os
import requests

class AIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"

    def generate_code(self, user_input: str) -> str:
        prompt = f"Generate only the code for the following request. Do not include any explanation, comments, or markdown:\n\n{user_input}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()
        try:
            return response_data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Error: Could not parse response"
