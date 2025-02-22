class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
        
        else:
            last = self.head 
            while last.next:
                last = last.next
            last.next = new_Node
    
    def insert(self, data):
        new_Node = Node(data)  # Create a new node
        if not self.head:  # If the linked list is empty
            self.head = new_Node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_Node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("NULL")
        
if __name__ == "__main__":
    linked_list = Linkedlist()
    n = int(input("Enter the number off element : "))
    for i in range(n):
        data = int(input(f"Enter the the data at possition {i+1} : "))
        linked_list = linked_list.append(data)
    print("Printing the list tail : ")
    linked_list.display()