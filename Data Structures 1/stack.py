class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return len(self.stack) == 0
    
    # if the stack has a fixed size
    """
    def isFull(self):
        if len(self.Stack) == 6:
            return True
        else:
            return False
    """

    def length(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty!"
        else:
            return self.stack[-1]
    

#TEST#

a = Stack() # I create my object
a.push(10) # insert the  element
a.push(23)
a.push(25)
a.push(27)
a.push(11)

print(a.length())
print(a.isEmpty())
print(a.stack)
print(a.peek())
a.push(30)

print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop()) # try to delete an element in a list without elements - the output will be underflow
print(a.isEmpty())

