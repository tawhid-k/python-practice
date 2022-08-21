class Node:
  def __init__(self, e = None, n = None):
    self.element = e
    self.next = n


class LinkedList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array. head will refer
  #  to the Node that contains the element from a[0]
  #  Else Sets the value of head. head will refer
  # to the given LinkedList

  # Hint: Use the type() function to determine the data type of a
    self.head = None
    if type(a) == list:
        cur_Node = self.head
        for i in a:
            if cur_Node == None:
                cur_Node = Node(i)
            else:
                cur_Node.next = Node(i)
                cur_Node = cur_Node.next
  # Count the number of nodes in the list
  
lst = LinkedList([1, 2, 3, 4, 5, 6])