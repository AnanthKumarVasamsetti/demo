class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
 

print("The listed commands are supported\n")
print("push <value>")
print("pop")
print("isEmpty")
print("top\n")

s = Stack()
while True:
    user_input = input().split()

    operation = user_input[0].strip().lower()
    
    if operation == "push":
        s.push(int(user_input[1]))
        print("Inserted: ",user_input[1],"\n")
    
    elif operation == "pop":
        if s.is_empty():
            print("Stack is empty.\n")
        else:
            print("Popped value: ", s.pop(), "\n")
    
    elif operation == "isempty":
        print(s.is_empty())
    
    elif operation == "top":
        if s.is_empty():
            print("Stack is empty\n")
        else:
            print("Top value: ",s.top(),"\n")
    
    else:
        print("Operation not supported\n")