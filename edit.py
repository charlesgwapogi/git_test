# Charles Anton A. Gemarino         BSIT II-B

class ArrayStack:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    #HELPER METHODS
    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def display(self):
        print(f"{self.stack}    |   TOP INDEX: {self.top}")

    def push(self, data):
        if self.is_full():
            print("Error: Stack Overflow")
            return
        
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Error: Stack Underflow")
            return
        
        self.stack[self.top] = None
        self.top -= 1

    def peek(self):
        if self.is_empty():
            print("Error: Stack Underflow")
            return
        
        return self.stack[self.top]

    def search(self, data):
        if self.is_empty():
            print("Error: Stack Underflow")
            return

        found_index = -1

        for i in range(self.capacity):
            if self.stack[i] == data:
                found_index = i
                break
            

        if found_index >= 0:
            print(f"{data} found at index: {found_index}")
        else:
            print(f"Error {data} not found in the stack")

    def menu(self):
        print("===============================================")
        print("                 SKAMBORDODI                   ")
        print("===============================================")
        print("[1] Push")
        print("[2] Pop")
        print("[3] Peek")
        print("[4] Display")
        print("[5] Search")
        print("[6] Clear")
        print("[7] Get")
        print("[0] Exit")
        print("===============================================")

        print(f"Is the Stack empty? {skambordi.is_empty()}")

    def clear(self):
        for i in range(self.top + 1):
            self.stack[i] = None

        self.top = -1
        print("\nStack Cleared")

    def get(self, index):
        if index < 0 or index > self.top:
            print("Error: Invalid Index")
            return None

        return self.stack[index]




if __name__ == "__main__":
    skambordi = ArrayStack()

    while True:
        skambordi.menu()

        choice = input("Enter your choice(1-5): ").strip()

        if choice == "1":
            data = input("Enter what you will push: ").strip()
            skambordi.push(data)

        elif choice == "2":
            skambordi.pop()

        elif choice == "3":
            print(f"Current Head: {skambordi.peek()}")

        elif choice == "4":
            skambordi.display()

        elif choice == "5":
            data = input("Search: ").strip()
            skambordi.search(data)

        elif choice == "6":
            skambordi.clear()

        elif choice == "7":
            data = input("Get from index: ").strip()
            print(f"Data from index{data}: {skambordi.get(int(data))}")

        elif choice == "0":
            break

        else:
            print("Error: Choice Not Valid")

    '''skambordi.display()
    skambordi.push(1)
    skambordi.push(2)
    skambordi.push(3)
    skambordi.push(4)
    skambordi.push(5)
    skambordi.display()
    skambordi.pop()
    skambordi.display()
    print(f"\nStack Head: {skambordi.peek()}")
    skambordi.search(10)
    skambordi.display()
    print(f"Retreive: {skambordi.get(1)}")'''