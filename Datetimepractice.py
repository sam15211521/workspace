from datetime import date, datetime

a = datetime.now()
dateandtime = a.strftime("%d/%m/%Y %H:%M:%S")


print(dateandtime)