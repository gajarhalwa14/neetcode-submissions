class Node():
    def __init__(self, key: str = "", children: Dict[str, Node] = None, is_end: bool = False):
        self.key = key
        self.children = children if children is not None else {}
        self.is_end = is_end

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        head = self.root
        for char in word:
            if char in head.children:
                head = head.children[char]
                continue
            head.children[char] = Node(char)
            head = head.children[char]

        head.is_end = True

        

    def search(self, word: str) -> bool:
        head = self.root
        for char in word:
            if char not in head.children:
                return False
            head = head.children[char]
        return head.is_end 

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for char in prefix:
            if char not in head.children:
                return False
            head = head.children[char]
        return True
        