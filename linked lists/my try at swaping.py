from msvcrt import LK_LOCK
from os import link


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
    
    def set_next_node(self, node):
        self.next_node = node
    
    

class Linkedlist:
    def __init__(self, value = None): #creates a head nodeto start a list
        self.head_node = Node(value)

    def get_head_node(self,): # shows what the head node is in memory
        return self.head_node
    
    def insert_beginning(self, new_value): 
       new_node = Node(new_value)
       new_node.set_next_node(self.head_node)
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

def testing(name_of_the_node,node_to_test):
    print(f'''----
TEST: This is the {name_of_the_node} : {node_to_test}
----
    ''')

def swaping_nodes(linked_nodes, val1, val2):
    if val1 == val2:
        print('values are the same, cannot continue')
        return

    node1 = linked_nodes.head_node
    node2 = linked_nodes.head_node
    node1_prev = None
    node2_prev = None
    print(f'this will swap nodes with the values of {val1} and {val2}\n')

    while node1 is not None: #this sets the memory access of node1 to the node with node.value = val1. 
        if node1.value == val1:
            break
        node1_prev = node1
        node1 = node1.next_node

    while node2 is not None: #this sets the memory access of node1 to the node with node.value = val1. 
        if node2.value == val2:
            break
        node2_prev = node2
        node2 = node2.next_node

    #if node1 or node2 are head nodes just set the origional as the head node, 
    # and set the previous node2 with the pointer for node1 or node2
    if node1_prev is None:
        linked_nodes.head_node = node2
    else:
        node1_prev.set_next_node(node2)
        


    if node2_prev is None:
        linked_nodes.head_node = node1
    else:
        node2_prev.set_next_node(node1)
    
    #updates the pointers of the nodes that were just changed
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
    
  
    


    #return(f'\n###\nRETURN : Node1 is {node1.value}, node2 is {node2.value} \n\nNode1_prev is {node1_prev.value}, node2 is {node2_prev.value} \n\nthe node pointed at by node1 is {node1.next_node.value}, the node pointed at by node2 is {node2.next_node.value}\n###\n')



def main():
    ll = Linkedlist(0)
    for i in range(1,10):
        ll.insert_beginning(i)

    print(ll.list_list())
    
    a = swaping_nodes(ll, 2, 3)


    print(ll.list_list())
    

main()