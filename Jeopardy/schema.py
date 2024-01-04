from whoosh.analysis import StemmingAnalyzer, CharsetFilter
from whoosh.fields import Schema, TEXT, ID, KEYWORD
from whoosh.support.charset import accent_map

custom_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)


def get_schema():
    return Schema(
        title=TEXT(stored=True),
        content=TEXT(analyzer=custom_analyzer, stored=True, phrase=True),
        categories=KEYWORD(stored=True, commas=True, scorable=True),
        id=ID(stored=True, unique=True)
    )
