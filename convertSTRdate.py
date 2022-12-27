from datetime import datetime
import time

date = '11/06/2022'
date2 = '13/06/2022'



dateCerto = datetime.strptime(date,'%d/%m/%Y')
dateCerto2 = datetime.strptime(date2,'%d/%m/%Y')

if dateCerto < dateCerto2:
    print('E maior')