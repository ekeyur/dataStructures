class MyHashTable:
    def __init__(self):
        self.me = 0

    def hash(self,value):
        if value == None:
            return "0"
        else:
            return value[0]+"!%"


myhash = MyHashTable()

print myhash.hash("apple")
