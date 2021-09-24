import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class TrieTree:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True
    
    def find(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word


class WordFinder:
    def __init__(self, words):
        self.trie = TrieTree()
        for w in words:
            self.trie.insert(w)

    def find(self, chars):
        res = []
        self.trie.find(chars)
        return res

wf = WordFinder(['apple', 'pplea', 'pear', 'pleap'])
res = wf.find('apple')
print(res)




            