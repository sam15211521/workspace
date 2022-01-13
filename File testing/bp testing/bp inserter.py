from datetime import datetime
import csv

systolic_phrase = input('Please enter systolic pressure ')

diastolic_phrase = input('Please enter diastolic pressure ')

pulse = input ('Please enter pulse rate ')
date = datetime.today()
date_str =date.strftime('%m/%d/%y %H:%M:%S')

fields = ['Date and Time', 'Systolic', 'Diastolic', 'pulse']

row = [date_str, systolic_phrase, diastolic_phrase, pulse]

with open('blood_pressure_chart.csv', 'a', newline ='') as chart:
    writing  = csv.writer(chart)
    writing.writerow(row)
    
    
