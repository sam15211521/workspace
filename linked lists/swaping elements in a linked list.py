import inspect

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def change_value(self, value):
        self.value = value
    
    def change_next_node(self, node):
        self.next_node = node

class Linkedlist:
    def __init__(self, value = None): #creates a head nodeto start a list
        self.head_node = Node(value)

    def get_head_node(self,): # shows what the head node is in memory
        return self.head_node
    
    def insert_beginning(self, new_value): 
       new_node = Node(new_value)
       new_node.change_next_node(self.head_node)
       self.head_node = new_node

    def list_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return string_list

def adding_to_the_linked_list():
    node_value = input('Please enter a value for the node:   ')
    eval(f'll.insert_beginning({node_value})')

ll = Linkedlist(0)

ll.insert_beginning(1)

ll.insert_beginning(2)

ll.insert_beginning(3)
ll.insert_beginning(4)
ll.insert_beginning(5)

node11 = Node(0, None)
node1_0 = Node(12, node11)

node12 = Node(15, node1_0)
node13 = Node(11,node12)
node14 = Node(5,node13)

def finding_node_values(value, node):
    node1 = node
    while node1.get_value() != value:
        if node1.get_next_node() is not None:
            print(f'The node located at {node1} has been skipped')
            node2  = node1.get_next_node()
            node1 = node2
        else:
            print('the value you are looking for is not found')
            return
        
        
    print(f'The node with value "{value}" is located at {node1}')
    return node1

def swaping_node_values(linked_list, val1, val2):
    node1 = linked_list.head_node # will equal to val1
    node2 = linked_list.head_node # will equal to val2
    node1_previous = None
    node2_previous = None
    
    while node1 is not None:
        if node1.get_value() == val1: #searching portion for node1
            break
        node1_previous = node1
        node1 = node1.get_next_node()

    while node2 is not None: #serching portion for node2
        if node2.get_value() == val2:
            break
        node1_previous = node2
        node2 = node2.get_next_node()
    
    if node1_previous is None:
        linked_list.head_node = node2
    else:
        node1_previous.change_next_node(node2)
    
    if node2_previous is None:
        linked_list.head_node = node1
    else:
        node2_previous.change_next_node(node1)
    
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

    if (node1 is None or node2 is None):
        print('Swap not possible - one or more element is not on the list')
        return
    
    
    print(node1, node2)

a = dir(node11)
print(a)


#swaping_node_values(ll, 0, 4)