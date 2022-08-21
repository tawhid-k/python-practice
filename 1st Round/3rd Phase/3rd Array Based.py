class arrayStack:
    def __init__(self, exp=None):
        self.exp = None
        self.st = []
        self.idx = -1
    def push(self, ch):
        self.st.append(ch)
        self.idx += 1
    def pop(self):
        if self.idx >= 0:
            self.st.pop(self.idx)
            self.idx -= 1
    def empty(self):
        if self.idx < 0:
            return True
        else:
            return False
    def top(self):
        if self.empty() == False:
            return self.st[self.idx]
        else:
            return None

def checkParanthesis(exp):
    stack = arrayStack()
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