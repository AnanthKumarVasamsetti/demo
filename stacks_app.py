class Stack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, x):    
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
        
    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return f'{self.stack}'

    def undo(self):
        curr_val = self.pop()
        if curr_val:
            self.temp_stack.append(curr_val)
        else:
            print("Nothing to undo")

    def redo(self):
        if len(self.temp_stack) == 0:
            print("Nothing to redo")
            return
        
        curr_val = self.temp_stack.pop()
        self.push(curr_val)

if __name__ == "__main__":
    print("The listed commands are supported\n")
    print("add <value>")
    print("undo")
    print("redo\n")

    stack = Stack()
    while True:
        user_input = input().split()

        operation = user_input[0].strip().lower()
        
        if operation == "add":
            stack.push(int(user_input[1]))
            
            print(stack, "\n")
        
        elif operation == "undo":
            stack.undo()
            print(stack, "\n")
        
        elif operation == "redo":
            stack.redo()
            print(stack, "\n")
        
        else:
            print("Operation not supported\n")