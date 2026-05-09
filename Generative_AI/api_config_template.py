"""
API configuration template for Generative AI integration.

This file shows how to load the Gemini API key safely from environment variables.
Do NOT write the real API key here.
Create a local .env file and add:
GEMINI_API_KEY=your_api_key_here
"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Add it to your local .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)