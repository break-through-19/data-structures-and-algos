"""
Insert and search costs O(key_length), however, the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N)
where N is the number of keys in Trie. There are efficient representations of trie nodes (e.g. compressed trie,
ternary search tree, etc.) to minimize the memory requirements of the trie.

"""

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False