class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def new_value(self, value):
        self.value = value


class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value): #inserts a new beginnig node to the front of the stack
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def adding_values(self):
        value = 0
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                value += current_node.get_value()
            current_node = current_node.get_next_node()
            print(value)


ll = (LinkedList(5))
ll.insert_beginning(6)
ll.insert_beginning(7)

ll.adding_values()
