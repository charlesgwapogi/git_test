class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(f" -> Commited: '{data}'.")
        return
        
    def pop(self):
        if self.is_empty():
            print("Error: Stack Undeflow.")
            return None
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.size -= 1
        print(f" -> Undid Commit: '{popped_node.data}'.")
        
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            print("Error: Stack is empty.")
            return
        
        return self.head.data
    
    def display(self):
        print("Commit History: ", end ="")
        
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print(f"None | Size :{self.size}")
        
    def menu(self):
        print("\n========================================")
        print("  GIT VERSION CONTROL: COMMIT MANAGER"   )
        print("========================================")
        print("[1] Commit Code(push)")
        print("[2] Undo Last Commit(pop)")
        print("[3] View Current Head(peek)")
        print("[4] Display Commit History")
        print("[5] Exit")
        print("========================================")
            
            
if __name__ == "__main__":
    my_stack = LinkedListStack()
    
    my_stack.push("Initial commit: Django initial pages setup")
    my_stack.push("feat: Added user authentication module")
    my_stack.push("fix: Resolved token expiration bug")
    
    while True:
        my_stack.menu()
        choice = input("Select an action(1-5): ")
        
        if choice == "1":
            commit_message = input("Commit: ")
            my_stack.push(commit_message)
        
        elif choice == "2":
            my_stack.pop()
            
        elif choice == "3":
            print(f"Current Head: {my_stack.peek()}")
            
        elif choice == "4":
            my_stack.display()
            
        elif choice == "5":
            print("\nExiting Program. Thank you. :)")
            break
        
        else:
            print("Error. Invalid Choice. :( )")
    
    
    
    
    
    
    '''print("\n====== PUSH ======")
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(2)
    my_stack.push(3)

    print("\n====== POP ======")
    my_stack.pop()
    
    print("\n====== PEEK =======")
    print(f"Current Head: '{my_stack.peek()}'")
    
    print("\n====== DISPLAY ======")
    my_stack.display()'''