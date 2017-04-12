class MyDictionary:
    def __init__(self):
        self.keys = []
        self.values = []

    def insert_element(self,key,element):
        # inserts the element into the Dictionary
        self.keys.append(key)
        self.values.append(element)

    def find_element(self,key):
        for k in range(0,len(self.keys)):
            if key == self.keys[k]:
                return self.values[k]
        #Finds the element associated with the key.
        # Returns None if key doesn't exist.

    def remove_element(self,key):
        # Finds element associated with key
        # Removes element if element is found
        for k in range(0,len(self.keys)):
            if key == self.keys[k]:
                del self.values[k]
                del self.keys[k]

    def get_keys(self):
        return self.keys;

    def elements(self):
        return self.values

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.values)



dictionary = MyDictionary()

dictionary.insert_element('email','tamby@hirewire.com')
dictionary.insert_element('password','chicken_nuggets')
dictionary.insert_element('phone','9737574181')

for key in dictionary.get_keys():
    print(key + "\t\t" + dictionary.find_element(key))

child_dictionary = MyDictionary()
child_dictionary.insert_element('another_value','test')

if dictionary.find_element('email') == 'tamby@hirewire.com':
    print ('yay')

print dictionary.keys
print dictionary.values

dictionary.remove_element("phone")
print "Updated Dictionary"

print dictionary.keys
print dictionary.values
