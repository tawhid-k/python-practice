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

  def countNode(self):
     count = 0
     cur_Node = self.head
     while cur_Node != None:
         count += 1
         cur_Node = cur_Node.next
     return count

  def printList(self):
     cur_node = self.head
     while cur_node != None:
         print(cur_node.element, end=" ")
         cur_node = cur_node.next
     print()
         
  def nodeAt(self, idx): 
     curIndex = 0
     curNode = self.head
     while curIndex != idx and curNode != None:
         curIndex += 1
         curNode = curNode.next
     return curNode
  
  def get(self, idx):
     curIndex = 0
     curNode = self.head
     while curIndex != idx and curNode != None:
         curIndex += 1
         curNode = curNode.next
     return curNode.element
  
    
  def set(self, idx, elem): # 99 100 2 3
    curIndex = 0
    curNode = self.head
    while curIndex != idx and curNode != None:
        curIndex += 1
        curNode = curNode.next
    
    if curIndex != idx:
        return None
    prevElem = curNode.element
    curNode.element = elem
    return prevElem

  def indexOf(self, elem): # 99  1  5   7
    curNode = self.head
    idx = 0 # 1  2
    while curNode.element != elem and curNode != None:
        idx += 1
        curNode = curNode.next
    if curNode.element == None:
        return -1
    else:
        return idx
        
  def contains(self, elem):
    curNode = self.head
    while curNode.element != elem:
        curNode = curNode.next
    if curNode.element == elem:
        return True
    else:
        return False

  def copyList(self): 
    a = []
    curNode = self.head
    while curNode != None:
        a.append(curNode.element)
        curNode = curNode.next
    return a

  def reverseList(self):
    a = self.copyList()
    b = []
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    return b
  
  def insert(self, elem, idx): #  90 100 5 200
    curNode = self.head
    curIdx = 0
    if idx == 0:
        curNode = self.head
        self.head = Node(elem, curNode)
        return
    while idx != curIdx and curNode != None:
        curIdx += 1
        prev = curNode
        curNode = curNode.next
    if curIdx < idx:
        return None
    else:
        prev.next = Node(elem, curNode)

  def remove(self, idx):
    curNode = self.head
    curIdx = 0
    if idx == 0:
        val = self.head.element
        self.head = self.head.next
        return val
    while idx != curIdx and curNode != None:
        curIdx += 1
        prev = curNode
        curNode = curNode.next
    if curIdx < idx:
        return None
    else:
        val = curNode.element
        prev.next = curNode.next
        return val

  #  1 2 3
  def rotateLeft(self):   
    val = self.head.element
    self.remove(0)
    self.insert(val, self.countNode())
  
  def rotateRight(self):
    val = self.get(self.countNode()-1)
    self.remove(self.countNode()-1)
    self.insert(val, 0)


print("////// Test 01 //////")
a1 = [10, 20, 30, 40]

h = LinkedList(a1)

h.printList()

print(h.get(0))





