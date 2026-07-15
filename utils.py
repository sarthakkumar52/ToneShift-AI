import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def rewrite_text(text, tone, length):

    prompt = f"""
{SYSTEM_PROMPT}

Rewrite the following text.

Tone:
{tone}

Length:
{length}

Text:
{text}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except ClientError as e:
        return f"❌ Gemini API Error:\n{e}"

    except Exception as e:
        return f"❌ Unexpected Error:\n{e}"