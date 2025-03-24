class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,item):
         self.stack.append(item)   
    
    def pop(self):
        if not self.is_empty():
           return self.stack.pop(-1)
        else:
           return 'stack is Empty'
    
    
    def is_empty(self):
        return len(self.stack)==0
    
    
my_Stack=Stack()

print(my_Stack.pop())

my_Stack.push('1')

my_Stack.push('2')

my_Stack.push('3')

my_Stack.push('2')
my_Stack.push('4')

print(my_Stack.pop())

print(my_Stack.stack)