import requests
import os.path
from download import download_wiki_abstract_data

# TODO run program 

if __name__ == '__main__':
    if not os.path.exists('data/enwiki-latest-abstract.xml.gz'):
        download_wiki_abstract_data()