import random

file = open('text.txt', 'w')
text = ''
num = int(input("Enter number: "))
for i in range(num):
    ch = random.randrange(97,123, 1)
    text += chr(ch)

file.write(text + '.')
file.close()
