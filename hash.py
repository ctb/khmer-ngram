import string

def hash(word):
    assert len(word) <= 8

    value = 0
    for n, ch in enumerate(word):
        value += ord(ch) * 256**n

    return value

class BloomFilter(object):
    allchars = "".join([ chr(i) for i in range(256) ])
    
    def __init__(self, tablesizes, k=8):
        self.tables = [ (size, [0] * size) for size in tablesizes ]
        self.k = k

    def add(self, word):
        val = hash(word)
        for size, ht in self.tables:
            ht[val % size] = 1

    def __contains__(self, word):
        val = hash(word)
        return all( ht[val % size] for (size, ht) in self.tables )

    def insert_text(self, text):
        for i in range(len(text) - self.k + 1):
            self.add(text[i:i+self.k])

    def occupancy(self):
        return [ sum(t)/float(len(t)) for _, t in self.tables ]

def first_next_word(bf, word):
    prefix = word[1:]
    for ch in bf.allchars:
        word = prefix + ch
        if word in bf:
            return ch, word
        
    return None, None

def retrieve_first_sentence(bf, start):
    word = start[-bf.k:]

    while 1:
        ch, word = first_next_word(bf, word)
        if ch is None:
            break

        start += ch

    return start

def next_words(bf, word):
    prefix = word[1:]
    for ch in bf.allchars:
        word = prefix + ch
        if word in bf:
            yield ch
        

def retrieve_all_sentences(bf, start):
    word = start[-bf.k:]

    n = -1
    for n, ch in enumerate(next_words(bf, word)):
        for sentence in retrieve_all_sentences(bf, start + ch):
            yield sentence

    if n < 0:
        yield start
        

if __name__ == '__main__':
    pass
