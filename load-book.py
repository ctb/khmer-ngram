import hash
import sys

N_HT=4
HT_SIZES=100e6

print 'creating data structure'

sizes = hash.get_n_primes_above_x(N_HT, int(HT_SIZES))
bf = hash.BloomFilter(sizes, 16)

print 'loading shredded reads'

for line in open(sys.argv[1]):
    bf.insert_text(line)

print 'retrieving paths that begin with "It was the best of times..."'
n = 0
for x in hash.retrieve_all_sentences(bf, "It was the best of times"):
    print (x,)
    if n > 8:
        break
    n += 1

print 'retrieving paths that begin with "age of foolishness"'
n = 0
for x in hash.retrieve_all_sentences(bf, "age of foolishness"):
    print (x,)
    if n > 8:
        break
    n += 1
    
