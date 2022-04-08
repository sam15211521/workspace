from turtle import clear


def clearing_blank_spaces(element_list):
    sorted_element_list =sorted(element_list)
    for character in sorted_element_list:
        if character == '':
            sorted_element_list.remove(character)
    return sorted_element_list

a =clearing_blank_spaces(['', 'a','f', 'b'])
print(a)