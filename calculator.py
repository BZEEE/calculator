
class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def make_empty(self):
        self.items = []
        

def infixToPostfix():
    file = open('infix.txt', 'r')
    expressions = file.read().splitlines()
    alphaOperand="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitOperand="0123456789"
    operators = {'(': 1, '-': 2, '+': 2, '*': 3,'/': 3, '%': 3}
    for expression in expressions:
        if expression != '':
            joined = expression.replace(' ', '')
            opStack = Stack()
            postfixList = []
            tokenList = list(joined)
          
            
            
            for token in tokenList:
                if token in alphaOperand or token in digitOperand:
                    postfixList.append(token)
                elif token == '(':
                    opStack.push(token)
                elif token == ')':
                    topToken = opStack.pop()
                    while topToken != '(':
                        postfixList.append(topToken)
                        topToken = opStack.pop()
                else:
                    while (not opStack.is_empty()) and (operators[opStack.peek()] >= operators[token]):
                        postfixList.append(opStack.pop())
                    opStack.push(token)
                    
            while not opStack.is_empty():
                postfixList.append(opStack.pop())
            postfixEval(postfixList)

    
    

def postfixEval(tokenList):
    operandStack = Stack()
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    print(float(operandStack.pop()))


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '%':
        return op1 % op2
# 8 + (3-7) *4  
    
infixToPostfix()