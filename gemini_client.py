import openai
import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        self.client = genai.GenerativeModel("gemini-1.5-flash",
                                      safety_settings=safety_settings)

    def chat(self, messages):
        response = self.client.generate_content(messages)
        response.resolve()

        return response
