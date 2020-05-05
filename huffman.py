class Node(object):
    ch = ""
    freq = 0
    code = None
    left = None
    right = None

    def __init__(self):
        self.right = None
        self.left = None

    def addData(self, ch, freq):
        self.ch = ch
        self.freq = freq

    def addLeft(self, left):
        self.left = left

    def addRight(self, right):
        self.right = right

    def getFreq(self):
        return self.freq

    def getCh(self):
        return self.ch

    def printData(self):
        print(self.ch, self.freq)


def search_min(dict_obj, min_freq):
    for ch, node in dict_obj.items():
        freq = node.getFreq()
        if(freq < min_freq):
            key = ch
            min_freq = freq
    dict_obj.pop(key)
    return node, key, min_freq


def dictChInDictObject(dict_of_ch):
    dict_obj = {}
    for ch, freq in dict_of_ch.items():
        node = Node()
        node.addData(ch, freq)
        dict_obj[ch] = node
    return dict_obj


def mergeNode(left, right):
    node = Node()
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


print(dict_of_ch)
dict_obj = dictChInDictObject(dict_of_ch)

temp_cntr = unique_ch_cntr - 1

for i in range(temp_cntr):
    node = Node()
    ch = ""
    freq = 0
    min_node_left, left_key, left_freq = search_min(dict_obj, max_freq)
    min_node_right, right_key, right_freq = search_min(dict_obj, max_freq)
    ch = ch + left_key + right_key
    freq += left_freq + right_freq
    node.addLeft(min_node_left)
    node.addRight(min_node_right)
    node.addData(ch, freq)
    dict_obj.setdefault(ch, node)
    print('left:', left_key, 'right:', right_key)
    node.printData()

# try:
#    dict_obj.popitem()
# except KeyError:
#    print("dict is empty")
# else:
#    print("succesful")
# for index in range(26):
#    val = list_of_ch[index]
#    if(val):
#        print(chr(97 + index),' - ', val)
