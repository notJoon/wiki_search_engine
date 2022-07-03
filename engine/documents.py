from collections import Counter
from dataclasses import dataclass
from engine.preprocessing import processing

@dataclass
class Abstract:
    """ wikipedia abstract structure """
    ID:         int 
    title:      str
    abstract:   str 
    url:        str 

    @property
    def text(self) -> None:
        return ' '.join([self.title, self.abstract])

    def processing(self) -> None:
        self.term_freq = Counter(processing(self.text))

    def term_frequency(self, term: str) -> int:
        return self.term_freq.get(term, 0)