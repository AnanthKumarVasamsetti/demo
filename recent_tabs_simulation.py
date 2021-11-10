class TabStack:
    def __init__(self):
        self.tabs = []
        self.tempStack = []

    def push(self, tab, undoIndex=-1, isUndo=False):
        if(isUndo):
            self.tabs.insert(undoIndex, tab)
            return

        self.tabs.append(tab)
        
    def is_empty(self):
        return len(self.tabs) == 0

    def close(self, tab):
        if self.is_empty():
            print("No tabs are opened")
            return
        if(tab not in self.tabs):
            print("There is no such tab")
            return
        
        currIndex = self.tabs.index(tab)
        self.tempStack.append((tab, currIndex))
        self.tabs.remove(tab)
        

    def undo(self):
        if len(self.tempStack) == 0:
            print("Nothing to undo")
            return
        
        (tab, lastIndex) = self.tempStack.pop()
        self.push(tab, lastIndex, isUndo=True)
    
    def __str__(self):
        return f'===== {self.tabs}'


if __name__ == "__main__":
    print("In this simulation the following operations are supported\n")
    print("open <value>")
    print("close <value>")
    print("undo\n")

    tabStack = TabStack()

    # tabStack.push("google")
    # tabStack.push("youtube")
    # tabStack.push("twitter")
    # #tabStack.push("wikipedia")

    # print(tabStack)

    # tabStack.close("youtube")

    # print(tabStack)

    # tabStack.undo()

    # print(tabStack)

    while True:
        userInput = input().split()

        operation = userInput[0].strip().lower()
        
        if operation == "open":
            if(len(userInput) == 1):
                print("Please provide a value")
            else:
                tabStack.push(userInput[1].lower())
                print(tabStack, "\n")
        
        elif operation == "close":
            if(len(userInput) == 1):
                print("Please provide a value")
            else:
                tabStack.close(userInput[1].lower())
                print(tabStack, "\n")
        
        elif operation == "undo":
            tabStack.undo()
            print(tabStack, "\n")
        
        else:
            print("Operation not supported\n")