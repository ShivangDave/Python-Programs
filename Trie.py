# Reference: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
from typing import Tuple
class Trie:
    def __init__(self,char: str):
        self.char = char
        self.children = []
        self.wordFinished = False
        self.counter = 1

    def add(self,root,word:str):
        node = root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = Trie(char)
                node.children.append(new_node)
                node = new_node
        node.wordFinished = True

    def findPrefix(self,root,prefix:str) -> Tuple[bool, int]:
        node = root
        if not root.children:
            return False,0
        for char in prefix:
            charNotFound = True
            for child in node.children:
                if child.char == char:
                    charNotFound = False
                    node = child
                    break
            if charNotFound:
                return False,0
        return True, node.counter
