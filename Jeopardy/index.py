from whoosh.index import create_in
from whoosh.writing import AsyncWriter
import os
from schema import get_schema
from parser import parse_articles

os.chdir('X:/Users/Bucur/PycharmProjects/pythonProject')

def create_index(index_dir, file_path):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    schema = get_schema()
    index = create_in(index_dir, schema)
    writer = AsyncWriter(index)

    for title, content, categories in parse_articles(file_path):
        writer.add_document(
            title=title,
            content=content,
            categories=categories,
            id=title.replace(' ', '_')
        )

    writer.commit()