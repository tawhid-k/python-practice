class Node:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self):
        pass
        
    def getHeight(self, node):
        if node == None:
            return 0
        else:
            return max(self.getHeight(node.left)+1, self.getHeight(node.right)+1)
    def getNodeLevel(self, node, curNode, level):
        if curNode == node:
            return level
        if curNode == None:
            return -1
        l = self.getNodeLevel(node, curNode.left, level+1)
        if l != -1:
            return l
        else:
            l = self.getNodeLevel(node, curNode.right, level+1)
            return l
    def preOrderTraversal(self, node):
        if node == None:
            return 
        else:
            print(node.data, end = ' ')
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
    def inOrderTraversal(self, root):
        if root == None:
            return 
        else:
            self.inOrderTraversal(root.left)
            print(root.data, end = ' ')
            self.inOrderTraversal(root.right)
    def postOrderTraversal(self, root):
        if root == None:
            return 
        else:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data, end = ' ')

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.left = b
a.right = c
b.left = d
b.right = e
e.right = f
c.left = g
c.right = h

tree = BinaryTree()
print(tree.getHeight(a))
print(tree.getNodeLevel(b, a, 0))
print(tree.getNodeLevel(e, a, 0))
print(tree.getNodeLevel(f, a, 0))
tree.preOrderTraversal(a)
print()
tree.inOrderTraversal(a)
print()
tree.postOrderTraversal(a)
