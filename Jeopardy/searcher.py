# searcher.py
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser, AndGroup
from whoosh.query import Term
from schema import get_schema


def search_index(index_dir, query):
    ix = open_dir(index_dir)
    qp = QueryParser("content", schema=get_schema())
    q = qp.parse(query)
    with ix.searcher() as s:
        results = s.search(q)
        print(results)
        for result in results:
            result_fields = result.fields()
            print(result_fields['title'])  # Print the title of the document
            print(result_fields['content'])
        return results

