import hashlib
hash = input();
with open("wordlist1.txt") as f:
    words = f.readlines()

words = [line.strip('\n') for line in words]

isDone = False

for word1 in words:
    if isDone:
        break
    for word2 in words:
        if hashlib.md5(word1 + word2).hexdigest() == hash:
            print "Done: " + word1 + word2
            isDone = True
            break
