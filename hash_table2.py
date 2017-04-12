class My_Hash_Table:
    def __init__(self):
        self.me = 0

    def hash(self,value):
        if value == None:
            return "Please input a value"
        else:
            return value[:3]


my_hash_table = My_Hash_Table()

print my_hash_table.hash("234-543-6549")
