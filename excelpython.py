from openpyxl import Workbook, load_workbook

wb = Workbook()

ws = wb.active

ws.title = "Data" #gives the name of the worksheet

for i in range(0,10):
    ws.append(['Time', 'Is', 'Great', '!']) #appends data to the end

#print(ws.value)
wb.save('tim1.xlsx') #saves the name as with a name
