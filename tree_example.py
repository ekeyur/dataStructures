class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = []

    def addChild(self,value):
        child_node = TreeNode(value)
        self.children.append(child_node)

    def clearChildren(self):
        self.children = []

n = TreeNode(10)
n.addChild(10)
n.addChild(5)
n.addChild(1)

n.children[0].addChild(1)

print (n.value)
print (n.children)

print (n.children[0].children)
