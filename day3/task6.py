sentence = "the quick brown fox jumps over the lazy dog"
l=sentence.split()
#print(l)
d={i:l.count(i) for i in l}
print(d)