import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin

def scrape_through_hs(grade: str, lesson: str, topic: str):
    base_url = "https://www.testkolik.com"
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    topic_url = f"{base_url}/{quote(grade.lower())}-sinif-{quote(lesson.lower().replace(' ', '-'))}-{quote(topic.lower().replace(' ', '-'))}.html"
    response = session.get(topic_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    test_button = soup.find('a', class_='btn btn-purple btn-lg', string=' TESTİ ÇÖZ ')
    if not test_button:
        print("Could not find the 'TESTİ ÇÖZ' button")
        return []

    test_url = urljoin(base_url, test_button['href'])
    response = session.get(test_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    questions = soup.find_all(class_='mtq_question mtq_scroll_item-1')
    scraped_questions = []

    for i, question in enumerate(questions, 1):
        question_number_elem = question.find(class_='question-number')
        if question_number_elem is None:
            print(f"Warning: Could not find question number for question {i}")
            question_number = f"Soru {i}"
        else:
            question_number = question_number_elem.text.strip()

        paragraphs = question.find_all('p')
        full_question = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])
        
        options_table = question.find(class_='mtq_answer_table')
        if options_table:
            options = options_table.find_all('tr')
            option_texts = []
            for option in options:
                option_letter = option.find(class_='mtq_letter').text.strip() if option.find(class_='mtq_letter') else ""
                option_text = option.find(class_='mtq_answer_text').text.strip() if option.find(class_='mtq_answer_text') else ""
                option_texts.append(f"{option_letter}. {option_text}")
        else:
            print(f"Warning: Could not find options table for question {i}")
            option_texts = []
        
        scraped_questions.append({
            "number": question_number,
            "full_text": full_question,
            "options": option_texts
        })

    return scraped_questions

def main():
    results = scrape_through_hs("10", "din-kulturu", "allah-insan-iliskisi")
    print(f"Scraped {len(results)} questions:")
    for question in results:
        print(f"\n{question['number']}:")
        print(question['full_text'])
        for option in question['options']:
            print(f"  {option}")

if __name__ == "__main__":
    main()
