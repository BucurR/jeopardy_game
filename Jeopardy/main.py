from Jeopardy.searcher import search_index
from index import create_index

def main():
    index_dir = './Jeopardy/data/indexdir'
    file_path = './Jeopardy/data/wiki-example.txt'
    create_index(index_dir, file_path)
    print("Searching index...")
    results = search_index(index_dir,'The body mass index (BMI)')


if __name__ == "__main__":
    main()