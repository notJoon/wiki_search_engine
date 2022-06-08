import math
from typing import List
from preprocessing import processing
from timer import timer

class Indexing:
    def __init__(self) -> None:
        self.index = {}
        self.documents = {}
    
    def index_document(self, document: str) -> None:
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            document.processing()

        for token in processing(document.text):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(document.ID)

    ## TF-IDF https://en.wikipedia.org/wiki/Tf%E2%80%93idf
    def document_frequency(self, token: str) -> int:
        return len(self.index[token].get(token, set()))

    # idf https://nlp.stanford.edu/IR-book/html/htmledition/inverse-document-frequency-1.html
    def inverse_document_frequency(self, token: str) -> float:
        return math.log10(len(self.documents) / self.document_frequency(token))

    def result(self, query: str) -> List[str]:
        return [self.index.get(token, set()) for token in query]
    
    @timer
    def search(self, query: str, search_type='AND', rank=False) -> List[str]:
        """search
        This method will return documents that contains words from the query.
        if requested rank them.

        Args:
        - query (str): the query string.
        - search_type ('AND' | 'OR'): do all quey terms have to match, or just one.
        - rank (bool): if True, rank result based on TF-IDF score
        """
        TYPES = ('AND', 'OR')
        search_type = search_type.upper()

        if search_type not in TYPES:
            return []
        
        processed_query = processing(query)
        results = self.result(processed_query)

        if search_type == 'AND':
            ## all tokens must be in the document
            documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
        
        if search_type == 'OR':
            ## only one tokens has to be in the document
            documents = [self.documents[doc_id] for doc_id in set.union(*results)]

        if rank:
            return self.rank(processed_query, documents)
        
        return documents
    
    def rank(self, processed_query: str, documents: List[str]) -> List[str]:
        results = []
        if not documents:
            return results 
        
        for document in documents:
            score = 0.0
            for token in processed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf 
            
            results.append((document, score))
        return sorted(results, key=lambda doc: doc[1], reverse=True)