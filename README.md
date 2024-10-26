# Web Scraper for Educational Content

This project contains a Python script that scrapes educational content from the website testkolik.com. It's designed to extract questions and their corresponding options for specific subjects and topics.

## Features

- Scrapes questions and options from testkolik.com
- Supports different grades, lessons, and topics
- Handles Turkish language content
- Uses BeautifulSoup for HTML parsing

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/salihfurkaan/intellifist-ai
   cd intellifist-ai
   ```

2. Install the required packages:
   ```
   pip install requests beautifulsoup4 google
   ```

  

## Usage

The main script is `src/data/bs_scraper.py`. You can run it directly:
```
python src/data/bs_scraper.py
```

Replace `GRADE`, `LESSON`, and `TOPIC` with your desired values.

## Function Description

The main function `scrape_through_hs(grade: str, lesson: str, topic: str)` takes three parameters:

- `grade`: The grade level (e.g., "10")
- `lesson`: The lesson name (e.g., "din-kulturu")
- `topic`: The specific topic (e.g., "allah-insan-iliskisi")

It returns a list of dictionaries, each containing:
- `number`: The question number
- `full_text`: The full text of the question
- `options`: A list of answer options

## Disclaimer

This script is for educational purposes only. Make sure you have the right to scrape content from the target website and comply with their terms of service.

## License

[MIT License](https://opensource.org/licenses/MIT)
