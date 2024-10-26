import requests
import json

def post(grade: str, lesson: str, topic: str, api_url: str = "http://localhost:8000/scrape"):
    """
    Send a POST request to the scraper API.

    Args:
    grade (str): The grade level.
    lesson (str): The lesson name.
    topic (str): The topic name.
    api_url (str): The URL of the API endpoint. Defaults to "http://localhost:8000/scrape".

    Returns:
    list: A list of scraped questions if successful.
    None: If the request fails.
    """
    payload = {
        "grade": grade,
        "lesson": lesson,
        "topic": topic
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def format_questions(questions):
    formatted = ""
    for question in questions:
        formatted += f"\n{question['number']}:\n"
        formatted += f"{question['full_text']}\n"

        for i, option in enumerate(question['options'], start=0):
            formatted += f"  {chr(65 + i)}. {option}\n"
        formatted += "\n"
    return formatted

if __name__ == "__main__":
    result = post("10", "din-kulturu", "allah-insan-iliskisi")
    if result:
        formatted_questions = format_questions(result)
        print(formatted_questions)
    else:
        print("Failed to scrape questions.")
