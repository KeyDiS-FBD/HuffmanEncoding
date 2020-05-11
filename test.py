import random

file = open('text.txt', 'w')
text = ''
num = int(input("Enter number: "))

for i in range(num // 80):
    for j in range(80):
        ch = random.randrange(97,123, 1)
        text += chr(ch)
    text += '\n'

for i in range(num % 80):
    ch = random.randrange(97,123, 1)
    text += chr(ch)
text+= '.'
file.write(text)
file.close()
