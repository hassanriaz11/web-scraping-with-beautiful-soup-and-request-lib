# Web Scraping with Python using BeautifulSoup and Requests

This project demonstrates how to perform **web scraping** using Python with the help of two powerful libraries:

- `requests` – to send HTTP requests and fetch web content.
- `BeautifulSoup` – to parse and extract data from HTML content.
- `lxml` – used as the parser for BeautifulSoup for efficient and fast parsing.

---

## Requirements
Before running the code, install the following libraries:

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
```

---

## What Does This Project Do?
This project teaches how to scrape both **static HTML pages** and **real websites**. Here's an overview of key concepts and steps:

### 1. **Sending HTTP Requests**
```python
import requests
response = requests.get('URL')
```
- Sends a request to the website.
- Retrieves the content (HTML), status code (e.g., 404), and headers.

### 2. **Parsing HTML**
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')
```
- `lxml` is the parser that helps convert HTML into a Python-readable structure.
- `soup.prettify()` prints formatted HTML.

### 3. **Reading from Local HTML Files (Optional)**
```python
with open('filename.html', 'r') as file:
    content = file.read()
soup = BeautifulSoup(content, 'lxml')
```
- Useful for offline testing and experimentation.

### 4. **Finding HTML Elements**
```python
tags = soup.find('h5')       # Finds the first occurrence
all_tags = soup.find_all('h5')  # Finds all <h5> tags
```
- Use `.text` to extract text content from tags.

### 5. **Iterating Over Elements**
```python
for course in all_tags:
    print(course.text)
```

### 6. **Scraping Specific Information (Example: Course Title and Price)**
```python
courses = soup.find_all('div', class_='course-card')
for course in courses:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]  # Extract price from anchor tag
    print(f"{course_name} costs {course_price}")
```

---

## Real Website Scraping
The code also demonstrates scraping real websites (e.g., timesjobs.com) to extract job listings, skills required, and job links. You can filter jobs based on familiarity with certain skills using basic string filtering techniques.

---

## Notes for Beginners
- `.find()` returns the **first** match.
- `.find_all()` returns **all** matches.
- `.text` gets clean human-readable content.
- `.split()` and `[-1]` help extract specific parts of text.
- `enumerate()` is used to get both index and value when looping.
- `if __name__ == '__main__':` ensures a block of code runs **only** when the script is executed directly (not when imported as a module).

---


Feel free to fork the repository, improve it, and use it for your projects!




