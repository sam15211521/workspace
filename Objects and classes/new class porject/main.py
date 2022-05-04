
import Element_class as Ele
from time import sleep


def electronegativities_prompt(): #This function is used to test the electronegativities of two elements based on their name or symbol.
        print('This program compairs two elements and gives their electronegativity diffrences,\nas well as their predicted bond type')
        sleep(1)
        prompt1_1text = 'What do you want to do? (type the number):\n 1) Enter elements \n 2)Exit\n\n'
        prompt1_1 = input(prompt1_1text) #first input

        while prompt1_1 != '1' and prompt1_1 != '2': #gives two options. to test or exit
            # start prompt 1.1 loop
            prompt1_1 = input('Please enter a number: \n 1) Enter elements \n 2)Exit\n\n')
            # end prompt 1.1 loop
        else:
            
            if prompt1_1 == '1': #loop that helps choose objects
                
                first_element = ''
                second_element = ''
                prompt1_flag = True
                
                input_data_loop = True
                
                while input_data_loop == True:
                    ## element choice input loop
                    
                    while prompt1_flag == True: 
                        ### element input loop
                                #need to add quit function to this part to make it easier
                        
                        first_element_input = input('\nPlease input the symbol or name of the first element you wish to compare.\n')
                        first_element_input_flag = True
                        while first_element_input_flag == True:
                        # First element input loop
                            for ele in Ele.element_list:
                                if first_element_input == ele.name or first_element_input == ele.symbol:
                                    
                                    first_element = ele.symbol
                                    print(f'\n \nThe element you have chosen is {ele.name} ({ele.symbol})\n')
                                    first_element_input_flag = False
                            if first_element_input_flag ==True:
                                first_element_input = input('Error: Element not found \n Please enter appropriate element symbol or element name')
                                

                        sleep(1)
                        
                        second_element_input = input('Please input the symbol or name of the second element you wish to compare.\n')
                        second_element_input_flag = True
                        while second_element_input_flag == True:

                        #Second element input loop
                            
                            for ele in Ele.element_list:
                                if second_element_input == ele.name or second_element_input == ele.symbol:

                                    second_element = ele.symbol
                                    print(f'\n \nThe second element you have chosen is {ele.name} ({ele.symbol})')
                                    second_element_input_flag = False
                                    #ends 2nd element input loop
                            if second_element_input_flag == True:
                                second_element_input = input('Error: Element not found \n Please enter appropriate element symbol or element name')
                        prompt1_flag = False

                        sleep(1)
                        # End prompt 1 loop



                    #after choosing element this code will run #to allow you to check if you have made the correct choices.
                    first_element_name = eval(eval('f"Ele.{first_element}.name"'))
                    second_element_name = eval(eval('f"Ele.{second_element}.name"'))

                    ending_input1_statment = f'\nThe Elements you have chosen are {first_element_name} ({first_element}), and {second_element_name} ({second_element})\n'
                    print(ending_input1_statment)
                    
                    #after this you determine if you have chosen correct

                    ending_input1 = input('\nAre these the elements you want to compair? Y/N\n').upper()
                    ending_input1_flag = True
                    while ending_input1_flag == True:
                        if ending_input1 == 'Y': # will end the input1 loop, prompt1 loop and input_data_loop and calls on Comparing Electronegativity method
                            ending_input1_flag = False
                            prompt1_flag = False
                            input_data_loop = False
                            Ele.Elements.compare_electronegativities(first_element, second_element)
                            sleep(3)
                            print('\n Thank you, choose another option\n')
                            sleep(3)
                            
                            

                        elif ending_input1 == 'N': # ends the input 1 loop sets prompt 1 flag to True and restarts the input data loop to restart prompt1 loop
                            ending_input1_flag = False
                            prompt1_flag = True
                            input_data_loop = True
                            
                        else:   #repeats loop for fixing.
                            print('\n###\n', ending_input1_statment)
                            ending_input1 = input('Are these the elements you want to compair? Please enter either Y or N\n')


                    



            elif prompt1_1 == '2':
                sleep(1)
                print('\n')
                return False
                    
                   #statment = f'The elements you have chosen are {}, ({}) and {}, ({})'



def entering_compounds(): #function used to create a list of compounds
    pass
 


def main():
    main_start_flag = True
    while main_start_flag == True:
        print('please choose the option you wish')
        main_start = input('\n1) find electronegativity diffrence/ types of chemical bond\n2) Enter a compound\n3)enter a chemical formula\n0) Exit\n\n')

        if main_start == '1':
            electronegativities_prompt()
        elif main_start == '0':
            print('Good Bye')
            sleep(.5)
            exit()
        elif main_start == '2':
            pass
        elif main_start =='3':
            pass

main()
#c = input('type an element symbol')


