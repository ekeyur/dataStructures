class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left_child_node = None
    self.right_child_node = None

class MyBinaryTree:
    def __init__(self):
        self.root_node = None

    def add(self, value):
        # Add the value into the tree.

        # If no root, then set value to root.
        if self.root_node == None:
            self.root_node = BinaryTreeNode(value)
            return

        current_node = self.root_node

        while current_node != None:
            if value >= current_node.value:
                if current_node.right_child_node == None:
                    current_node.right_child_node = BinaryTreeNode(value)
                    break
                else:
                    current_node = current_node.right_child_node
            else:
                if current_node.left_child_node == None:
                    current_node.left_child_node = BinaryTreeNode(value)
                    break
                else:
                    current_node = current_node.left_child_node


b = MyBinaryTree()
b.add(10)

b.add(11)
