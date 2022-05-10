import time
start_time = time.time()
a = 1000000
declst = [i for i in range(a+1)]
hexlst = [hex(i).replace('0x','') for i in range(a+1)]

def lst_to_string(lst1, lst2):
    return_string = ''
    index = 0
    for entry in lst1: 
        return_string += f'{lst1[index]} | {lst2[index]}\n'
        index +=1

    return return_string

with open('The_list.txt','w') as f:
    f.write(str(lst_to_string(declst, hexlst)))
    


#print(lst)
#print()
#print(adapthexlst)

print(f'process finished {time.time() - start_time}')