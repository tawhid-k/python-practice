class Node:
  def __init__(self, e=None, n=None, p=None):
    self.element = e
    self.next = n
    self.prev = p

class DoublyList:
  
  def __init__(self, a):
      self.head = None
      if type(a) == list:
          for i in a: 
              if self.head == None:
                 self.head = Node(i)   
                 cur_Node = self.head
              else:
                  cur_Node.next = Node(i)
                  cur_Node.next.prev = cur_Node
                  cur_Node = cur_Node.next
  
  def countNode(self):
      count = 0
      cur_Node = self.head
      while cur_Node != None:
          count += 1
          cur_Node = cur_Node.next
      return count
  
  def forwardprint(self):
    cur_node = self.head
    while cur_node != None:
        print(cur_node.element, end=" ")
        cur_node = cur_node.next
    print()

  def backwardprint(self):
    cur_node = self.head
    while cur_node.next != None:
        cur_node = cur_node.next
    while cur_node != None:
        print(cur_node.element, end=' ')
        cur_node = cur_node.prev
    print()

  def nodeAt(self, idx):
    curIndex = 0
    curNode = self.head
    while curIndex != idx and curNode != None:
        curIndex += 1
        curNode = curNode.next
    return curNode

  def indexOf(self, elem):
    curNode = self.head
    idx = 0 # 1  2
    while curNode.element != elem and curNode != None:
        idx += 1
        curNode = curNode.next
    if curNode.element == None:
        return -1
    else:
        return idx

  def insert(self, elem, idx):
      curNode = self.head
      curIdx = 0
      if idx == 0:
          curNode = self.head
          self.head = Node(elem, curNode)
          curNode.prev = self.head
          return
      while idx != curIdx and curNode != None:
          curIdx += 1
          prev = curNode
          curNode = curNode.next
      if curIdx < idx:
          return None
      else:
          prev.next = Node(elem, curNode, prev)
          if curNode != None:
           curNode.prev = prev.next
          
  def remove(self, idx):
    curNode = self.head
    curIdx = 0
    if idx == 0:
        val = self.head.element
        self.head = self.head.next
        self.head.prev = None
        return str(val)
    while idx != curIdx and curNode != None:
        curIdx += 1
        prev = curNode
        curNode = curNode.next
    if curIdx < idx:
        return None
    else:
        val = curNode.element
        prev.next = curNode.next
        if curNode.next != None:
          curNode.next.prev = prev
        return str(val)


print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.