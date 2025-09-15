

class stack:
    def __init__(self):
        self.data = []

    def push(self, item): #add to stack
        self.data.append(item)

    def pop(self): #remove from stack
        if self.is_empty():
            raise IndexError("Pop From Stack is Null")
        return self.data.pop()
    
    def peek(self): #view top of stack
        if self.is_empty():
            raise IndexError("Peek From Stack is Null")
        return self.data[-1]
        
    def is_empty(self): #check if stack is empty
        return len(self.data) == 0
    
    def size(self): #return size of stack
        return len(self.data)
    
    def __repr__(self):
        return f"Stack({self.data})"
    
class Menu:
    def __init__(self):
        self.stack = stack()

    def menu(self):
        while True:
            print("\nPlease Select menu")
            print("Q = Quit ,A = Push, D = Pop, M = Pee, S = Size")
            choice = input("input choice : ").strip().upper()
            if choice == "Q":
                print("Good Bye")
                break
            self.check_menu(choice)
            self.display()

    def check_menu(self, choice):
        if(choice == "A"):
            self.push()
        elif(choice == "D"):
            self.pop()
        elif(choice == "M"):
            self.peek()
        elif(choice == "S"):
            self.check_size()
        else:
            print("Invalid choice, please try again.")


    def push(self):
        item = input("input item to push :")
        # IF you want integers : item = int(item)
        self.stack.push(item)
        print(f"Pushed {item}")

    def pop(self):
        try:
            item = self.stack.pop()
            print(f"Popped {item}")
        except IndexError as e:
            print(e)

    def peek(self):
        try:
            item = self.stack.peek()
            print(f"Peeked {item}")
        except IndexError as e:
            print(e)

    def check_size(self):
        print(f"Size is {self.stack.size()}")

    def display(self):
        print("Current Stack:", self.stack)

if __name__ == "__main__":
    Menu().menu()


#menuStack = Menu()
#menuStack.menu()
#new_stack = stack()
#new_stack.push(0)
#new_stack.push(1)
#new_stack.push(2)
#new_stack.push(3)

#print(new_stack)
#print("Peek is ", new_stack.peek())
#print("Pop is ", new_stack.pop())
#print(new_stack)
#print("Size is ", new_stack.size())