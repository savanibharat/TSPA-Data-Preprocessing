import operator, time, string
import matplotlib.pyplot as plt

folder = ''
f = open(folder + 'shakesphere.txt', 'r')

start = time.time()

huck = {}
for line in f:
    line = line.split()
    for word in line:
        word = word.lower()
        new_word = word.translate(string.maketrans("",""), string.punctuation)
        if new_word in huck:
            huck[new_word] += 1
        else:
            huck[new_word] = 1

sorted_huck = sorted(huck.iteritems(), key=operator.itemgetter(1), reverse = True)
elapsed = time.time() - start

print 'Run took ', elapsed, ' seconds.'
print 'Number of distinct words: ', len(sorted_huck)

# Printing and plotting most popular words
npopular = 50
x = range(npopular)
y = []
for pair in range(npopular):
    y = y + [sorted_huck[pair][1]]
    print sorted_huck[pair]

plt.plot(x, y, 'ro')
plt.xlabel('Word ranking')
plt.ylabel('Word frequency')
plt.show()