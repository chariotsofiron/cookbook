"""Trie data structure.

https://en.wikipedia.org/wiki/Trie.
aka prefix-tree
"""


class TrieNode:
    """Trie node."""

    def __init__(self) -> None:
        """Constructs a node of a trie."""
        # char -> Trie
        self.nodes: dict[str, TrieNode] = {}
        self.is_leaf = False

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie."""
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def contains(self, word: str) -> bool:
        """Returns true if the word in in the Trie."""
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def delete(self, word: str) -> None:
        """Removes a word from the Trie."""

        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0

            char = word[index]
            char_node = curr.nodes.get(char)
            if not char_node:
                return False  # char not in current node

            if delete_curr := _delete(char_node, word, index + 1):
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr

        _delete(self, word, 0)


def test() -> None:
    """Tests the Trie."""
    trie = TrieNode()

    trie.insert("apple")
    trie.insert("app")
    trie.insert("apples")

    assert trie.contains("apple")
    assert trie.contains("app")
    assert trie.contains("apples")
    assert not trie.contains("appl")
