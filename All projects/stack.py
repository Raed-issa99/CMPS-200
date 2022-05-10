class Stack:
    """Construscts an empty list that represents a stack"""
    def __init__(self,list = []):
        self.stack = [i for i in list]
    """Adds an element to the top of the stack"""
    def push(self,element):
        self.stack.append(element)
    """Pops an element at the top of the list"""
    def pop(self):
        self.stack.pop()
    """returns a boolean that represents if a list is empty"""
    def is_empty(self):
        return self.stack == []
    """returns the length of a stack"""
    def __len__(self):
        return len(self.stack)

r = Stack(['hello','hey','hi'])
print(r.stack) #Creates a stack with these elements

r.push('hello')
print(r.stack) #adds hello to the top of the stack

r.push('Happy ')#adds happy to the top of the stack
print(r.stack)

r.pop() #pops the last element
print(r.stack) 

print(r.is_empty())
