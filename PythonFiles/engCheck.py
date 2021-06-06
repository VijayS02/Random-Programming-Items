import re
import operator
text = raw_input("What is the text?\n")
text = re.sub(r'[^\w\s]','',text)
text = text.split(' ')
print(text)
for i in text:
    if(i=="\n"):
        text.pop(text.index(i))


words = {}
for i in text:
    word = i.lower()
    if(word in words):
        if(word == 'and'):
            print('and')
        words[word] = words[word]+1
    else:
        words[word]=1

sorted_x = sorted(words.items(), key=operator.itemgetter(1))

for i in range(1,20):
    print('Word: '+str(sorted_x[len(sorted_x)-i][0]) +' has '+str(sorted_x[len(sorted_x)-i][1]) +' occurances.')


