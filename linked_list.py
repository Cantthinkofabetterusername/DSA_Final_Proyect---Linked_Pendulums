class Node:
    def __init__(self, node_data):
        self.node_data = node_data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None
        self.circulified = False
        self.trasversed = False

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = Node(data)
        elif self.head != None and self.head.next == None:
            self.head.next = Node(data)
            self.head.next.prev = self.head
            self.tail = self.head.next
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def delete(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def circulify(self):
        if self.circulified == False:
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail.next = self.head
            self.head.prev = self.tail
        
        self.circulified = True

    def traverse(self):
        if self.circulified:
            loop = True
            current_node = self.head
            while loop:
                if current_node.next == self.head:
                    loop = False
                    self.trasversed = True
                    return current_node
                else:
                    current_node = current_node.next

    def move_next(self):
        if self.trasversed == False:
            self.current_node = self.traverse()
        self.current_node = self.current_node.next

    def move_prev(self):
        if self.trasversed == False:
            self.current_node = self.traverse()
        self.current_node = self.current_node.prev