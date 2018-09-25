# from textwrap import dedent
# import sys


class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = []

    def __repr__(self):
        pass

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

    def set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        hashkey = self._hash_key(key)
        if self.hashtable[hashkey] is None:
            self.hashtable[hashkey] = [value]
        else:
            # TODO: deal with collisions
            pass
        return True

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hashkey = self._hash_key(key)
        # TODO: deal with multiple values for this hashkey
        return self.hashtable[hashkey]

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        pass


def repeated_word(string):
    """ Return the first repeated word
    """
    h = HashTable()
    for word in string:
        word = word.lower()
        if len(h.get(word)) > 0:
            for ea in h.get(word):
                if ea == word:
                    return word
        h.set(word)  # only happens if it wasn't a match
    return None


if __name__ == '__main__':
    string = input('Input words :>')
    result = repeated_word(string)
    print(result)
