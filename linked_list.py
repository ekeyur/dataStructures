class Node:
    def __init__(self,value,previous_node,next_node):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

class QueueLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def queue(self,value):
        new_node = Node(value)
        if self.head_node == None and self.tail_node == None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            old_tail = self.tail_node
            self.tail_node = new_node
            new_node.previous_node = old_tail
            old_tail.next_node = new_node

    def dequeue(self):
        item = self.head_node
        self.head_node = item.next_node
        self.head_node.previous_node = None
        return item.value

Node(1)

ll = QueueLinkedList()
