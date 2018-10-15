from .binary_tree import Node, BinaryTree
# import sys


class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = [None for _ in range(size)]

    def __str__(self):
        return f'HashTable | Size: {self.table_size}'

    def __repr__(self):
        return f'<HashTable | Size: {self.table_size}>'

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value=True):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """

        hashkey = self._hash_key(key)
        if self.hashtable[hashkey] is None:
            bt = BinaryTree({key: value})
            self.hashtable[hashkey] = bt
        elif not self.hashtable[hashkey].get(key):
            self.hashtable[hashkey].insert(key, value)
        return True  # if key already present, returned true and left alone

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hashkey = self._hash_key(key)
        if self.hashtable[hashkey] is None:
            return False
        return self.hashtable[hashkey].get(key)

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hashkey = self._hash_key(key)
        if self.hashtable[hashkey] is None:
            return False
        bt = self.hashtable[hashkey]
        if bt.root.val == key:
            self.hashtable[hashkey] = None
        return bt.delete(key)
    # end of remove
