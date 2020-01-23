check = open('tweet.txt', 'r')
word1 = check.read()
word2 = "hi"

set1 = set(word1.split(' '))
set2 = set(word2.split(' '))

print word1
print set1 == set2


counter = 5;
count = open('count.txt', 'w')
count.write(str(counter))
count.close
count = open('count.txt', 'r')
print count.read()