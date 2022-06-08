import requests

def download_wiki_abstract_data():
    URL = r'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz'
    with requests.get(URL, stream=True) as r:
        r.raise_for_status()
        with open('data/enwiki-latest-abstract.xml.gz', 'wb') as f:
            for i, chunk in enumerate(r.iter_content(chunk_size=1024*1024)):
                f.write(chunk)
                if i % 10 == 0:
                    print(f'Downloaded {i}MB', end='\r')

if __name__ == '__main__':
    download_wiki_abstract_data()