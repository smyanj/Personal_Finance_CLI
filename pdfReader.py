import pdfplumber
import random 
from openai import OpenAI
import os 
from dotenv import load_dotenv

key = os.getenv("OPEN_AI_KEY")
client = OpenAI(api_key=key)


def extract_quote(pdf_path="Tii.PDF", page_number=0):
    with pdfplumber.open(pdf_path) as pdf:
        if page_number >= len(pdf.pages):
            return "Page number out of range."

        page = pdf.pages[page_number]
        text = page.extract_text()

        if not text:
            return "No text found on the page."

        prompt = f"""
You're an investing expert and financial writer.

Here is an excerpt from *The Intelligent Investor*:

{text}

From this text, extract a single impactful quote (no commentary, just the quote).
"""

        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])

        return response.choices[0].message.content.strip()