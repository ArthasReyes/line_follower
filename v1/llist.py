class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def display(self):
        counter = 0
        current = self.head
        while current:
            print(counter, current.data)
            current = current.next
            counter+=1
            
    def pop(self):
        current = self.head
        self.head = current.next
        return current.data
    
