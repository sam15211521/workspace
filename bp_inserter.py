from openpyxl import Workbook, load_workbook
from datetime import datetime

systolic_phrase = input('Please enter systolic pressure ')

diastolic_phrase = input('Please enter diastolic pressure ')

pulse = input ('Please enter pulse rate ')
date = datetime.today()
date_str =date.strftime('%m/%d/%y %H:%M:%S')

wb = load_workbook('blood_pressure_sheet.xlsx')

ws =wb.active
ws.append([date_str, systolic_phrase, diastolic_phrase, pulse])



wb.save('blood_pressure_sheet.xlsx') 


