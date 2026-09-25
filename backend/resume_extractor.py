import os
from dotenv import load_dotenv
from groq import Groq

from resume_schema import ResumeData


load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GroqApiKey not set.")
client = Groq(api_key=api_key)

def extract_resume(markdown_text: str) -> ResumeData:
    try:
        response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": """
                You are an expert resume information extraction system.

Extract JSON information ONLY from the supplied resume Markdown.

Rules:
1. Do not invent information.
2. Do not convert technologies mentioned only in project descriptions into global skills unless they are explicitly listed as skills.
3. If information is missing, use null or an empty list.
4. Preserve the meaning of the original resume.
5. Extract all education entries.
6. Extract all projects.
7. Extract all internships and work experience.
8. Extract all explicitly mentioned technical skills.
9. Extract certifications when present.
10. URLs should be copied exactly when available.
""",
            },
            {
                "role": "user",
                "content": f"""
Extract structured information from this resume:

--- RESUME MARKDOWN START ---

{markdown_text}

--- RESUME MARKDOWN END ---
""",
            },
        ],
        response_format={"type": "json_object"},
    )
    except Exception as e:
         raise RuntimeError(f"Groq resume extraction failed.: {e}") from e

    raw_json = response.choices[0].message.content

    if not raw_json:
        raise ValueError("Groq returned an empty response. Unable to extract resume data.")

    return ResumeData.model_validate_json(raw_json)