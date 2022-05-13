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

ll = Linkedlist('For the bees!')

ll.insert_beginning('All the Honey')

ll.insert_beginning('And thus we go')



#print(ll.list_list())

def checking_next_node(): #this prints the value and a node list that can be copy pasted into the value of another node
    print(f'\n### \n{ll.head_node.value}')
    #print(ll.head_node)
    string = 'll.head_node'
    print(f'located at {string}\n###')
    prompt = input('do you want to find the next node value?    Y/N   ')
    
    if prompt.upper() == 'Y':
        while eval(string+'.next_node') != None:
            string += '.next_node'
            new_value = eval(string+'.value')
            #new_node = eval(string+'.next_node')
            print(f'\n ### \nThe next node value is {new_value} \n at: {string} \n ### \n')
    else:
        return
#print(ll.head_node.next_node.value)
checking_next_node()

#print(ll.head_node.next_node.next_node.value)