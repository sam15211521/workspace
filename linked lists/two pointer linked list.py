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

def counting_index_of_nodes(node_list):
    dict_of_nodes ={} #will return this which will consist of {index: node}
    list_of_nodes =[]
    list_of_index =[]
    current_node = node_list.get_head_node()
    i = 0
    while current_node is not None:
        list_of_nodes.append(current_node)
        list_of_index.append(i)
        i+=1
        current_node = current_node.get_next_node()
    print(f'TEST: {list_of_index}')




def main():
    ll = Linkedlist(0)
    for i in range(1,11):
        ll.insert_beginning(i)
    print(ll.list_list())
    print('###')
    counting_index_of_nodes(ll)

    

main()