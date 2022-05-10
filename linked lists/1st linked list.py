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

def main():
    ll = Linkedlist(9)
    ll.insert_beginning(3)
    flag = True
    while flag == True:
        adding_to_the_linked_list()
        continue_statment = input('add more?   Y/N\n')
        if continue_statment.upper() == 'Y':
            continue
        else:
            flag = False

    print(ll.list_list())

main()