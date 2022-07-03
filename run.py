import requests
import os.path
from download import download_wiki_abstract_data
from engine.timer import timer
from engine.indexing import Indexing
from load import load_documents

@timer
def index_documents(documents, index):
    for i, document in enumerate(documents):
        index.index_document(document)
    if i % 5000 == 0:
        print(f'Index {i} documents', end="")
    return index


if __name__ == '__main__':
    if not os.path.exists('data/enwiki-latest-abstract.xml.gz'):
        download_wiki_abstract_data()
    
    index = index_documents(load_documents(), Indexing())
    print(f'Index contains {len(index.documents)} documents')

    index.search('London Beer Flood', search_type='AND')