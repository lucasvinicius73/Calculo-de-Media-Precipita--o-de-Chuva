from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd
from IPython.display import display

table = pd.read_csv('DataSet/data2.csv')

def parse_float(seriesList):
    listValues = []
    for value in seriesList:
        value = float(value)
        listValues.append(value)
    return listValues

parse_float(table['Temp. Ins. (C)'])
parse_float(table['Temp. Max. (C)'])
parse_float(table['Temp. Min. (C)'])
parse_float(table['Umi. Ins. (%)'])
parse_float(table['Umi. Max. (%)'])
parse_float(table['Umi. Min. (%)'])
parse_float(table['Pto Orvalho Ins. (C)'])
parse_float(table['Pto Orvalho Max. (C)'])
parse_float(table['Pto Orvalho Min. (C)'])
parse_float(table['Pressao Ins. (hPa)'])
parse_float(table['Pressao Max. (hPa)'])
parse_float(table['Pressao Min. (hPa)'])
parse_float(table['Vel. Vento (m/s)'])
parse_float(table['Dir. Vento (m/s)'])
parse_float(table['Raj. Vento (m/s)'])
parse_float(table['Radiacao (KJ/m²)'])
parse_float(table['Chuva (mm)'])

# table['Data'] = table['Data'].astype(datetime.date)

def parse_for_datetime(seriesDate):
    Datalist = []
    for index,value in seriesDate.items():
        valueDate = datetime.strptime(value,'%d/%m/%Y')
        Datalist.append(valueDate)
    return Datalist

table['Data'] = parse_for_datetime(table['Data'])
mounth06 = (table[table['Data'] < datetime.strptime('01/07/2021','%d/%m/%Y')])
mean06 = float( "{:.2f}".format(mounth06['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 06 : {mean06}")

mounth07 = (table[table['Data'] < datetime.strptime('01/08/2021','%d/%m/%Y')])
mean07 = float( "{:.2f}".format(mounth07['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 07 : {mean07}")

mounth08 = (table[table['Data'] < datetime.strptime('01/09/2021','%d/%m/%Y')])
mean08 = float( "{:.2f}".format(mounth08['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 08 : {mean08}")

mounth09 = (table[table['Data'] < datetime.strptime('01/10/2021','%d/%m/%Y')])
mean09 = float( "{:.2f}".format(mounth09['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 09 : {mean09}")

mounth10 = (table[table['Data'] < datetime.strptime('01/11/2021','%d/%m/%Y')])
mean10 = float( "{:.2f}".format(mounth10['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 10 : {mean10}")

mounth11 = (table[table['Data'] < datetime.strptime('01/12/2021','%d/%m/%Y')])
mean11 = float("{:.2f}".format(mounth11['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 06 : {mean11}")

mounth12 = (table[table['Data'] < datetime.strptime('01/01/2022','%d/%m/%Y')])
mean12 = float("{:.2f}".format(mounth12['Temp. Ins. (C)'].mean()) )
print(f"Media do Mês 12 : {mean12}")

meses = [mean06,mean07,mean08,mean09,mean10,mean11,mean12]
labels = ['06/2021','07/2021','08/2021','09/2021','10/2021','11/2021','12/2021']

fig = plt.figure(figsize = (10, 5))
chartBar = plt.bar(x=labels,height=meses,width=0.4)

plt.bar_label(chartBar, label_type="edge")

plt.yticks(range(0,35,15))
plt.xlabel("Meses")
plt.ylabel("Media das precipitações")
plt.title("Grafico das medias das precipitações em 6 meses")
plt.show()