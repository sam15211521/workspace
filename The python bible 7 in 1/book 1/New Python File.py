


def listing_numbers():
    global lst 
    lst = [1,2,5,672,43,25,7,23,98]
    
#listing_numbers()
#print(lst)
#for x in lst:
    #print(x)       #global practice


# devide by zero practice
def devide_by_zero(num):
    result = num / 0
    return result

# try:
#     a = devide_by_zero(3)

# except:
#     a = 1
#     print('you devided by zero')


### opening and closing files #####

def opening_a_file(file_to_open = 'C:/Users/sam15/textfile.txt'):
    with open(file_to_open, 'a') as file:
        file.write('\nhello file')

    # with open(file_to_open, 'r') as file:
    #     print(file.read())
        

# opening_a_file('csv_file.csv')

### working with strings ###

# name, age = 'John', 25

# print('%s is my name! \n I am %d years old!' % (name, age))


text1 = 'hello world'
# for index, value in enumerate(text):
#     print(index, value)
#print(text)

# for i in text[::2]:
#     print(i)


def string_functions():
    ### practice on the stirng functions ###
    text ='I like you and you like me!'
#print(text.find('you'))
    sep = '.'
    sep_text = sep.join(text)
    #print(sep_text)
    names = 'John, Max, bob, Anna'
    name_list = names.split(',')
    

string_functions()

