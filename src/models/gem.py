import os
import sys
import google.generativeai as genai

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.data.api_client import post, format_questions

os.environ["GEMINI_API_KEY"] = "AIzaSyDvLwMOWc86STuzEIq-MdiBWK5d-gDX4bc"

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 0.85,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

result = post("10", "din-kulturu", "allah-insan-iliskisi")
if result:
    formatted_questions = format_questions(result)
else:
    formatted_questions = "Failed to fetch questions."

prompt = f"""You are a professional educator preparing questions for students. You are given the following questions and your task is to create similar questions in that format.

Here are the example questions:

{formatted_questions}

Please create new questions following the same format and style as the examples provided."""

response = chat_session.send_message(prompt)

print(response.text)
