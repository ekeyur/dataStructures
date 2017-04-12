class My_Hash_Table:
    def __init__(self):
        self.me = 0

    def hash(self,value):
        hash = 1
        if value == None:
            return "Please input a value"
        else:
            arr = value.split(" ")
            for i in range(0,len(arr)):
                print arr[i]
                hash *= ord(arr[i][0].lower())-97
            return hash

my_hash_table = My_Hash_Table()

print my_hash_table.hash("Karon Blake")
