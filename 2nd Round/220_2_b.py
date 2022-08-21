class Node:
  def __init__(self, e = None, n = None):
    self.element = e
    self.next = n


class LinkedList:
  
  def __init__(self, a):
      self.head = None
      if type(a) == list:
          for i in a: # a = [99, 1, 2, 3, 4, 5]
              if self.head == None:
                 self.head = Node(i)   #Node(99)
                 cur_Node = self.head
              else:
                  cur_Node.next = Node(i)
                  cur_Node = cur_Node.next


def addElements(node):
    if node == None:
        return 0
    else:
        return node.element + addElements(node.next)

myList = LinkedList([3,4,5,6,7])
print(addElements(myList.head))
