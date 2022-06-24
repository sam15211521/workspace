import csv
def list_into_csv(dict):
    with open('Chemistry_Closet_Inventory.csv', mode = 'a', newline= '') as csvfile:
        fieldnames = ['Compound Name', 'Amount', 'Date Purchased']
        file_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for compound in dict:
            file_writer.writerow(compound)

listing = [{'Compound Name' : 'cyclohexane', 'Amount' : 45, 'Date Purchased' : '9/2/1992'}, {'Compound Name' : 'ethanol', 'Amount' : 69, 'Date Purchased' : '9/2/2002'}]

list_into_csv(listing)