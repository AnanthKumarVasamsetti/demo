class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
    
    def front(self):
        return self.items[-1]
 

print("The listed commands are supported\n")
print("enqueue <value>")
print("dequeue")
print("isEmpty")
print("front\n")

q = Queue()
while True:
    user_input = input().split()
    operation = user_input[0].strip().lower()

    if operation == "enqueue":
        q.enqueue(int(user_input[1]))
        print("Inserted: ",user_input[1],"\n")
    
    elif operation == "dequeue":
        if q.is_empty():
            print("Queue is empty.\n")
        else:
            print("Dequeued value: ", q.dequeue(),"\n")
    
    elif operation == "isempty":
        print(q.is_empty(),"\n")
    
    elif operation == "front":
        if q.is_empty():
            print("Queue is empty.\n")
        else:
            print("Front element is: ", q.front(), "\n")
    
    else:
        print("Operation not supported\n")