import sys
import random

READLEN=40
OVERLAP=16

book_data = open(sys.argv[1]).read()
paras = book_data.split('\r\n\r\n')
paras = [ x.replace('\r\n', ' ').strip() for x in paras ]
paras = [ x.replace('\n', ' ').strip() for x in paras ]
print paras

x = []
for p in paras:
    for pos in range(0, len(p), READLEN - OVERLAP):
        read = p[pos:pos+READLEN]
        x.append(read)

random.shuffle(x)
for p in x:
    print p
