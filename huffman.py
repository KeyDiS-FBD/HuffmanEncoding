class Node(object):
    ch = ""
    freq = 0
    code = ''
    left = None
    right = None

    def __init__(self):
        self.left = None
        self.right = None

    def addData(self, ch, freq):
        self.ch = ch
        self.freq = freq

    def addLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def addRight(self, right):
        self.right = right

    def getRight(self):
        return self.right

    def getFreq(self):
        return self.freq

    def getCh(self):
        return self.ch

    def addCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def printData(self):
        print(self.ch, self.freq)

# Seachin in dictionary of nodes with frequency


def search_min(dict_obj, min_freq):
    min_node = None
    for ch, node in dict_obj.items():
        freq = node.getFreq()
        if(freq < min_freq):
            key = ch
            min_freq = freq
            min_node = node
    dict_obj.pop(key)
    return min_node, key, min_freq

# Create a new dictionary of objects from source dictionary


def dictChInDictObject(dict_of_ch):
    dict_obj = {}
    for ch, freq in dict_of_ch.items():
        node = Node()
        node.addData(ch, freq)
        dict_obj[ch] = node
    return dict_obj

# no comments


def mergeNode(left, right):
    node = Node()
    node.addLeft(left)
    node.addRight(right)
    return node

# Tree traverse with creating code of this symbol


def treeTraversal(root, code, encode_dict):
    if(root == None):
        return
    root.addCode(code)
    treeTraversal(root.getLeft(), code + '1', encode_dict)
    treeTraversal(root.getRight(), code + '0', encode_dict)
    if(checkChild(root)):
        ch = root.getCh()
        encode_dict[ch] = code


def checkChild(root):
    if(root.getLeft() == None and root.getRight() == None):
        return 1
    else:
        return 0


def printTreeCode(root):
    if(root == None):
        return
    print(root.getCh(), '-', root.getCode())
    printTreeCode(root.getLeft())
    printTreeCode(root.getRight())


def printEncodedText(text, encode_dict):
    encoded_text = ''
    for ch in text:
        encoded_text += encode_dict[ch]
    print("Encoded text:", encoded_text)


def printChFreqCode(dict_of_ch, encode_dict):
    for ch, freq in dict_of_ch.items():
        code = encode_dict[ch]
        print("Symbol:", ch, "Frequency:", freq, "Code:", code)


def checkText(text):
    if(text[0] == '.'):
        print("Empty text")
        exit()
    if(text[-1] != '.'):
        print("Not found End of Input\nIf you wanna encode this type 'encode'")
        print("If you wanna add text type 'input'")
        command = input()
        if(command == 'input'):
            text = text + input()
            text = checkText(text)
        elif(command == 'encode'):
            text = text + '.'
        else:
            print("Not found End of Input and the correct command is not specified")
            exit()

    # check len(text) include End of Input
    # If len of characters > 4000 stop

    if(len(text) > 4001):
        print("Too many characters\nIf encode this type 'continue'")
        print("Else type 'end'")
        command = input()
        if(command == 'end'):
            exit()
        elif(command == 'continue'):
            text = text[:4000] + '.'
    return text


alphabet = 'abcdefghijklmnopqrstuvwxyz'
# text = input()
# text = checkText(text)

file = open('text.txt', 'r')

text = file.read()
text = text.replace('\n', '')
checkText(text)
text = text.replace('.', '')

max_freq = len(text)
code = ''
dict_of_ch = {}
unique_ch_cntr = 0


for ch in alphabet:
    cntr = text.count(ch)
    if(cntr):
        dict_of_ch[ch] = cntr
        unique_ch_cntr += 1

if(unique_ch_cntr == 0):
    print("Empty input")
    exit()

dict_obj = dictChInDictObject(dict_of_ch)
for i in range(unique_ch_cntr - 1):
    ch = ""
    freq = 0
    min_node_left, left_key, left_freq = search_min(dict_obj, max_freq)
    min_node_right, right_key, right_freq = search_min(dict_obj, max_freq)
    ch = ch + left_key + right_key
    freq += left_freq + right_freq
    node = mergeNode(min_node_left, min_node_right)
    node.addData(ch, freq)
    dict_obj.setdefault(ch, node)

key, root = dict_obj.popitem()
encode_dict = {}
if(checkChild(root)):
    root.addCode('0')
    encode_dict[root.getCh()] = '0'
else:
    treeTraversal(root, code, encode_dict)
# print("Tree Print")
# printTreeCode(root)
printChFreqCode(dict_of_ch, encode_dict)
printEncodedText(text, encode_dict)
