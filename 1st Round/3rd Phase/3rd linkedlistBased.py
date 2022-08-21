class Node:
  def __init__(self, e = None, n = None):
    self.element = e
    self.next = n


class linkedlistStack:
  def __init__(self, a=None):
      self.head = None
      if type(a) == list:
          for i in a: # a = [99, 1, 2, 3, 4, 5]
              if self.head == None:
                 self.head = Node(i)   #Node(99)
                 cur_Node = self.head
              else:
                  cur_Node.next = Node(i)
                  cur_Node = cur_Node.next
  def push(self, ch):
      if self.head == None:
         self.head = Node(ch)   
      else:
          curNode = self.head
          self.head = Node(ch, curNode)
  def pop(self):
      if self.head != None:
          self.head = self.head.next
  def top(self):
      return self.head.element
  def empty(self):
      if self.head == None:
          return True
      else:
          return False

def checkParanthesis(exp):
    stack = linkedlistStack()
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            stack.push(exp[i])
        elif exp[i] == ']':
            if stack.empty() == False and stack.top() == '[':
                stack.pop()
            elif stack.empty() == False:
                print("Error at character #"+str(exp.find(stack.top())+1)+ " "+ stack.top() +" not closed")
                return
            else:
                print("Error at character #"+str(i+1)+" ] is not opened")
                return
        elif exp[i] == '}':
            if stack.empty() == False and stack.top() == '{':
                stack.pop()
            elif stack.empty() == False:
                print("Error at character #"+str(exp.find(stack.top())+1)+ " "+ stack.top() +" not closed")
                return
            else:
                print("Error at character #"+str(i+1)+" } is not opened")
                return
        elif exp[i] == ')':
            if stack.empty() == False and stack.top() == '(':
                stack.pop()
            elif stack.empty() == False:
                print("Error at character #"+str(exp.find(stack.top())+1)+ " "+ stack.top() +" not closed")
                return
            else:
                print("Error at character #"+str(i+1)+" ) is not opened")
                return
    if stack.empty() == True:
        print('The expression is correct')
    else:
        print('The expression is not correct.' + stack.top()+" has no closing")
         
exp1 = '1+2*(3/4)'
exp2 = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
exp3 = '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14'
exp4 = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'

checkParanthesis(exp1)
checkParanthesis(exp2)
checkParanthesis(exp3)
checkParanthesis(exp4)