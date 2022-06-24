import csv
#from tkinter import ttk
from tkinter import *

from pyparsing import col
# def adding_chemicals():
#     chemical_name = input('\nWhat is the chemical name?\n')
#     chemical_amount = input(f'\nHow much of{chemical_name} is present?\n')
#     mlorg = input('mL or g')
#     is_date = input('what is the date')
#     final_lst = []


    
def clear_and_reload_window(widget_lst, widgets_to_load, location_dic):
    for widget in widget_lst:
        widget.grid_forget 
    
    for widget in widgets_to_load:
        pass
    pass

def delete_temp_text(widget):
    widget.delete(0, END)

def temp_dict(name, ammount, date, mg_or_ml): 
    temp_dict = {}
    temp_dict['Compound Name'] = name
    temp_dict['Amount'] = ammount
    temp_dict['Date Purchased'] = date
    temp_dict['mg or ml'] = mg_or_ml
    return temp_dict

def stringing_lists(lst):
    string = ''
    for li in lst:
        string+= f'{li}\n'
    return string

def list_into_csv(dict):
    with open('Chemistry_Closet_Inventory.csv', mode = 'a', newline= '') as csvfile:
        fieldnames = ['Compound Name', 'Amount',  'mg or ml', 'Date Purchased']
        file_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for compound in dict:
            file_writer.writerow(compound)

def configuring_the_button():
    pass

def get_radio_button(variable):
    choice = variable
    if choice == 'mg':
        output = 'mg'
    elif choice == 'ml':
        output = 'ml'
    else:
        output = 'Invlid selection'
    return output


def root_window():
    lst_of_compound_dicts=[]
    temp_compound = []
    #calling the window
    root = Tk()
    root.geometry('280x150')
    root.title('Chemical Inventory')
    root.resizable(True,True)

    root.grid_rowconfigure(1,weight=1 )
    root.grid_columnconfigure(1,weight = 1)
    
    #this is where first level frames go
    button_frame = LabelFrame(root, padx = 10, pady = 10)
    greeting_frame = LabelFrame(root, padx = 10, pady = 10)
    
    greeting_frame.grid(column = 1, row = 1)
    button_frame.grid(column = 1, row = 2)
    ##

    #this is where the compound input screen goes
    instruction = 'Enter the name of the compound in the first box, \nthe amount in the second box\n and if applicable add the date purchused in the thrid box.\n use the buttons to indicate amount in mg or ml'
    instructions = Label(root, text = instruction)
    compound_name_frame = LabelFrame(root, padx = 10, pady = 10, text = 'Compound Name',width=200)
    compound_ammount_frame = LabelFrame(root, padx = 10, pady = 10, text = 'Compound Ammount')
    date_purchused = LabelFrame(root, padx = 10, pady = 10, text = 'Date Purchused')
    mg_or_ml_frame = Frame(root,padx = 10, pady = 10)
    input_button_frame = Frame(root, padx = 10, pady = 10)
       
    
    #radio buttons for selecting miligrams or mililiters
    var_string = StringVar()
    mg_or_ml_radio_button1 = Radiobutton(mg_or_ml_frame, text = 'mg', value= 'mg', variable=var_string)
    mg_or_ml_radio_button2 = Radiobutton(mg_or_ml_frame, text = 'ml', value= 'ml', variable=var_string)
    
    #input of compound name
    compound_name_input = Entry(compound_name_frame, width=200)
    compound_ammount_input = Entry(compound_ammount_frame)
    compound_date_input = Entry(date_purchused)


    ###

    # These widgets are in the view_all_new_entries section
    stringed_list = StringVar()
    new_entries_frame = Canvas(root)
    new_entries = Label(new_entries_frame, textvariable= stringed_list )
    new_entries_scroll_bar = Scrollbar(new_entries_frame, orient = 'vertical' )
    
    new_entries_back_buttion = Button(root, text = 'Back', padx = 10, pady =2, command = lambda : [ new_entries.grid_forget(),
                                                                                                    new_entries_back_buttion.grid_forget(),
                                                                                                    new_entries_scroll_bar.grid_forget(),
                                                                                                    new_entries_frame.grid_forget(),
                                                                                                    root.geometry('750x200'),
                                                                                                    instructions.grid(column =2, row = 1),
                                                                                                    instructions.grid_rowconfigure(0, weight=1),
                                                                                                    instructions.grid_columnconfigure(5, weight=5),
                                                                                                                        
                                                                                                    compound_name_frame.grid(column=1, row=2),
                                                                                                    compound_name_frame.grid_rowconfigure(1, weight=1),
                                                                                                    compound_name_frame.grid_columnconfigure(1, weight=1), 
                                                                                                    compound_name_input.grid(column = 1, row = 1),
                                                                                                                        
                                                                                                    compound_ammount_frame.grid(column= 2, row= 2),                                                                                                                                                                                                             compound_name_frame.grid(column=1, row=2),
                                                                                                    compound_ammount_frame.grid_rowconfigure(1, weight=1),
                                                                                                    compound_ammount_frame.grid_columnconfigure(1, weight=1),
                                                                                                    compound_ammount_input.grid(column=1, row=1),

                                                                                                    mg_or_ml_frame.grid(column = 4, row = 2),
                                                                                                    mg_or_ml_frame.grid_rowconfigure(1, weight=1),
                                                                                                    mg_or_ml_frame.grid_columnconfigure(1, weight=1),
                                                                                                    mg_or_ml_radio_button1.grid(column =1, row=1),
                                                                                                    mg_or_ml_radio_button2.grid(column =1, row=2),
                                                                                                      
                                                                                                    date_purchused.grid(column=3, row=2),
                                                                                                    date_purchused.grid_rowconfigure(1, weight=1),
                                                                                                    date_purchused.grid_columnconfigure(1, weight=1),
                                                                                                    compound_date_input.grid(column=1, row=1),

                                                                                                    input_button_frame.grid(column=1, row=3, columnspan=3),
                                                                                                    input_button_frame.grid_rowconfigure(1, weight=1),
                                                                                                    input_button_frame.grid_columnconfigure(1, weight=1),
                                                                                                      
                                                                                                    save_entry_button.grid(column=1,row=1, padx = 30),
                                                                                                    view_new_entries.grid(column=2,row=1, padx = 30),    
                                                                                                    comment_new_entries.grid(column = 3, row=1, padx = 30),                                                                                           
                                                                                                    exit_button_input.grid(column=4,row=1, padx = 30)
                                                                                                    ])
  
    ###

    #input  buttons go here
        #this button will save the entry into a list of compounds.
    save_entry_button = Button(input_button_frame, text = 'Save entry', padx=10, pady=2, command=lambda:[lst_of_compound_dicts.append(temp_dict(compound_name_input.get(), 
                                                                                                                                                compound_ammount_input.get(),
                                                                                                                                                str(compound_date_input.get()), 
                                                                                                                                                var_string.get()),)
                                                                                                                                                ])

        #this button will exit the current screen and pull up a list of all new entries that have been made
    view_new_entries = Button(input_button_frame, text = 'View all new entries', padx=10, pady=2, command=lambda : [instructions.grid_forget(),
                                                                                                                 compound_name_frame.grid_forget(),
                                                                                                                 compound_ammount_frame.grid_forget(),
                                                                                                                 date_purchused.grid_forget(),
                                                                                                                 input_button_frame.grid_forget(),
                                                                                                                
                                                                                                                 stringed_list.set(stringing_lists(lst_of_compound_dicts)),

                                                                                                                 new_entries_frame.grid(column=1,row=1),
                                                                                                                 new_entries.grid(column=1, row=1),
                                                                                                                 new_entries_scroll_bar.grid(column=2,row=1),
                                                                                                                 new_entries_back_buttion.grid(column=1,row=2)
                                                                                                                 ])
        # this button will commit all entries to the csv file needs a popup window to warn user what will happen.
    comment_new_entries = Button(input_button_frame, text = 'Comment new entries', padx = 10, pady= 2, command =lambda: comment_new_entries.config(list_into_csv(lst_of_compound_dicts)))#list_into_csv(lst_of_compound_dicts))
        #this button will exit the program completly and not save progress. needs to have a window popup warning what will hapen
    exit_button_input = Button(input_button_frame, text = "Exit", padx=10, pady=2, command=root.destroy)

    #first buttons 

    greeting = Label(greeting_frame, text ='Hello what do you want to do?').grid(column= 1, row= 1)
    exit_button =  Button(button_frame, text = "Exit", padx=5, pady=2, command=root.destroy)
    continue_button = Button(button_frame, text = "Enter \ncompound", padx=5, pady=2, command=lambda:[button_frame.grid_forget(),
                                                                                                      greeting_frame.grid_forget(),
                                                                                                      root.geometry('750x200'),
                                                                                                      instructions.grid(column =2, row = 1),
                                                                                                      instructions.grid_rowconfigure(0, weight=1),
                                                                                                      instructions.grid_columnconfigure(5, weight=5),
                                                                                                                        
                                                                                                      compound_name_frame.grid(column=1, row=2),
                                                                                                      compound_name_frame.grid_rowconfigure(1, weight=1),
                                                                                                      compound_name_frame.grid_columnconfigure(1, weight=1), 
                                                                                                      compound_name_input.grid(column = 1, row = 1),
                                                                                                                        
                                                                                                      compound_ammount_frame.grid(column= 2, row= 2),                                                                                                                                                                                                             compound_name_frame.grid(column=1, row=2),
                                                                                                      compound_ammount_frame.grid_rowconfigure(1, weight=1),
                                                                                                      compound_ammount_frame.grid_columnconfigure(1, weight=1),
                                                                                                      compound_ammount_input.grid(column=1, row=1),
                                                                                                      
                                                                                                      date_purchused.grid(column=3, row=2),
                                                                                                      date_purchused.grid_rowconfigure(1, weight=1),
                                                                                                      date_purchused.grid_columnconfigure(1, weight=1),
                                                                                                      compound_date_input.grid(column=1, row=1),

                                                                                                      input_button_frame.grid(column=1, row=3, columnspan=3),
                                                                                                      input_button_frame.grid_rowconfigure(1, weight=1),
                                                                                                      input_button_frame.grid_columnconfigure(1, weight=1),
                                                                                                      
                                                                                                      save_entry_button.grid(column=1,row=1, padx = 30),
                                                                                                      view_new_entries.grid(column=2,row=1, padx = 30),    
                                                                                                      comment_new_entries.grid(column = 3, row=1, padx = 30),                                                                                           
                                                                                                      exit_button_input.grid(column=4,row=1, padx = 30),

                                                                                                     mg_or_ml_frame.grid(column = 4, row = 2),
                                                                                                     mg_or_ml_frame.grid_rowconfigure(1, weight=1),
                                                                                                     mg_or_ml_frame.grid_columnconfigure(1, weight=1),
                                                                                                     mg_or_ml_radio_button1.grid(column =1, row=1),
                                                                                                     mg_or_ml_radio_button2.grid(column =1, row=2),
                                                                                                      ])

    #first level buttons
    
    exit_button.grid(pady =5, column = 1, row=1)
    continue_button.grid(padx = 5, pady =5, column = 2, row=1)

    ###

    #mainloop function
    root.mainloop()

def main():
    root_window()

main()