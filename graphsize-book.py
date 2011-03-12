import hash
import sys

N_HT=4
HT_SIZES=100e6

print 'creating data structure'

sizes = hash.get_n_primes_above_x(N_HT, int(HT_SIZES))
bf = hash.BloomFilter(sizes, 9)

print 'loading shredded reads'

for line in open(sys.argv[1]):
    bf.insert_text(line)

###

CUTOFF=100

#print bf.occupancy()
for line in open(sys.argv[1]):
    graphsize = hash.count_connected_graph(bf, line[:bf.k], CUTOFF)

    if graphsize >= CUTOFF:
        print graphsize, line,
