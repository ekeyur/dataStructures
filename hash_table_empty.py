class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def my_hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        if(self.buckets[self.my_hash(value)] == None):
            self.buckets[self.my_hash(value)] = []
        self.buckets[self.my_hash(value)].append(value)
        # Inserts value into the correct bucket.

    def exists(self, value):
        # Returns true if the value exists in the bucket.
        index = self.my_hash(value)
        if self.buckets[index] == None:
            return False
        else:
            for i in range(0,len(self.buckets[index])):
                if value == self.buckets[index][i]:
                    return True    
            return False


hash_table = MyHashTable()
hash_table.insert('Hello World')
hash_table.insert('Bob')
hash_table.insert('Cathy')
hash_table.insert('Zebra')

print(hash_table.exists('Hello World'))
print(hash_table.exists('Keyur'))

print(hash_table.buckets)
