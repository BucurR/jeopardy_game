import re


def parse_articles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    articles = content.split('\n\n\n')
    for article in articles:
        title_match = re.search(r'\[\[(.*?)\]\]', article)
        title = title_match.group(1) if title_match else 'No Title'
        categories_match = re.search(r'CATEGORIES: (.*)', article)
        categories = categories_match.group(1) if categories_match else ''
        content = re.sub(r'\[\[.*?\]\]', '', article)
        content = re.sub(r'CATEGORIES: .*', '', content)
        yield title, content.strip(), categories.strip()
