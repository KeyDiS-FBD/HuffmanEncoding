class Node(object):
    ch = None
    freq = None
    code = None
    left = None
    right = None
    def __init__(self, ch, freq):
         
        self.ch = ch
        self.freq = freq
    def addLeft(self, left):
        self.left = left
    def addRight(self, right):
        self.right = right
    def printData(self):
        print(self.ch, self.freq)

def search_min(temp_dict, alphabet, min_freq):
    for ch, freq in temp_dict.items():
        if(freq < min_freq):
            key = ch
            min_freq = freq
    temp_dict.pop(key)
    return key, min_freq


def dictChInDictObject(dict_of_ch):
    dict_obj = {}
    for ch, freq in dict_of_ch.items():
        node = Node(ch, freq)
        dict_obj[ch] = node
    return dict_obj

def mergeNode(left, right):
    node = Node(None, None)
    node.addLeft(left)
    node.addRight(right)
    return node


alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input()
list_of_ch = [0] * 26
dict_of_ch = {}
unique_ch_cntr = 0
for ch in alphabet:
    cntr = text.count(ch)
    if(cntr):
        dict_of_ch[ch] = cntr
        unique_ch_cntr += 1
temp_dict = dict_of_ch.copy()
max_freq = len(text)

#for index in range(26):
#    cntr = text.count(chr(97 + index))
#    if(cntr):
#        list_of_ch.insert(index, cntr)
print(dict_of_ch)

for i in range(unique_ch_cntr):
    key, freq = search_min(temp_dict, alphabet, max_freq)
    print(key, freq)
#for index in range(26):
#    val = list_of_ch[index]
#    if(val):
#        print(chr(97 + index),' - ', val)

