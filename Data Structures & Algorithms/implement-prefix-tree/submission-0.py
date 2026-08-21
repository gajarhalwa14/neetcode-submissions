class Node():
    def __init__(self, key: str = "", children: Dict[str, Node] = None):
        self.key = key
        self.children = children if children is not None else {}

class PrefixTree:

    def __init__(self):
        self.root = Node()
        self.words = {}

    def insert(self, word: str) -> None:
        head = self.root
        for char in word:
            if char in head.children:
                head = head.children[char]
                continue
            head.children[char] = Node(char)
            head = head.children[char]

        self.words[word] = True

        

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for char in prefix:
            if char not in head.children:
                return False
            head = head.children[char]
        return True
        