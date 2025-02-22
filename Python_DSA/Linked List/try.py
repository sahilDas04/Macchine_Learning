class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None
        
    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
                last.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("Null")
        
if __name__ == "__main__":
    linke = Linked()
    n = int(input("Enter the lengt of the Linked List : "))
    for i in range(n):
        data = int(input(f"Enter the data at possiton {i+1} : "))
        linke = linke.insertAtHead(data)
    print("Printing Linked List")
    linke.display()