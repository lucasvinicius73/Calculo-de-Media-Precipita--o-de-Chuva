from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv('DataSet/data.csv', sep=';')

def parse_float(seriesList):
    listValues = []
    for value in seriesList:
        if type(value) == float:
            listValues.append(value)
        if type(value) == str:
            value = value.replace(',', '.')
            value = float(value)
            listValues.append(value)
    return listValues

table['Temp. Ins. (C)'] = parse_float(table['Temp. Ins. (C)'])
table['Temp. Max. (C)'] = parse_float(table['Temp. Max. (C)'])
table['Temp. Min. (C)'] = parse_float(table['Temp. Min. (C)'])
table['Umi. Ins. (%)'] = parse_float(table['Umi. Ins. (%)'])
table['Umi. Max. (%)'] = parse_float(table['Umi. Max. (%)'])
table['Umi. Min. (%)'] = parse_float(table['Umi. Min. (%)'])
table['Pto Orvalho Ins. (C)'] = parse_float(table['Pto Orvalho Ins. (C)'])
table['Pto Orvalho Max. (C)'] = parse_float(table['Pto Orvalho Max. (C)'])
table['Pto Orvalho Min. (C)'] = parse_float(table['Pto Orvalho Min. (C)'])
table['Pressao Ins. (hPa)'] = parse_float(table['Pressao Ins. (hPa)'])
table['Pressao Max. (hPa)'] = parse_float(table['Pressao Max. (hPa)'])
table['Pressao Min. (hPa)'] = parse_float(table['Pressao Min. (hPa)'])
table['Vel. Vento (m/s)'] = parse_float(table['Vel. Vento (m/s)'])
table['Dir. Vento (m/s)'] = parse_float(table['Dir. Vento (m/s)'])
table['Raj. Vento (m/s)'] = parse_float(table['Raj. Vento (m/s)'])
table['Radiacao (KJ/m²)'] = parse_float(table['Radiacao (KJ/m²)'])
table['Chuva (mm)'] = parse_float(table['Chuva (mm)'])

table.interpolate(inplace=True)


print(f"Quantidade Valores nulos: {table.isnull().sum().sum()}")


def parse_for_datetime(seriesDate):
    Datalist = []
    for index,value in seriesDate.items():
        valueDate = datetime.strptime(value,'%d/%m/%Y')
        Datalist.append(valueDate)
    return Datalist

table['Data'] = parse_for_datetime(table['Data'])

def rainiest_day():
    for_day = table.groupby('Data')['Chuva (mm)'].sum()
    largest = for_day.max()
    for day,valor in for_day.items():
        if valor == largest:
            print(f"O dia que mais choveu: {datetime.date(day)} valor: {valor:.02f} mm")

rainiest_day()


def mean_for_months(nameColunm):
    meanlist = []

    mounth06 = table.loc[(table['Data'] >= datetime.strptime('01/06/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/07/2021','%d/%m/%Y'))]
    mean06 =  (mounth06[nameColunm].mean())
    meanlist.append(mean06)
    print(f"Media do Mês 06 : {mean06}")

    mounth07 = table.loc[(table['Data'] >= datetime.strptime('01/07/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/08/2021','%d/%m/%Y'))]
    mean07 = ( mounth07[nameColunm].mean())
    meanlist.append(mean07)
    print(f"Media do Mês 07 : {mean07}")

    mounth08 = table.loc[(table['Data'] >= datetime.strptime('01/08/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/09/2021','%d/%m/%Y'))]
    mean08 = ( mounth08[nameColunm].mean())
    meanlist.append(mean08)
    print(f"Media do Mês 08 : {mean08}")

    mounth09 = table.loc[(table['Data'] >= datetime.strptime('01/09/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/10/2021','%d/%m/%Y'))]
    mean09 = ( mounth09[nameColunm].mean())
    meanlist.append(mean09)
    print(f"Media do Mês 09 : {mean09}")

    mounth10 = table.loc[(table['Data'] >= datetime.strptime('01/10/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/11/2021','%d/%m/%Y'))]
    mean10 = ( mounth10[nameColunm].mean())
    meanlist.append(mean10)
    print(f"Media do Mês 10 : {mean10}")

    mounth11 = table.loc[(table['Data'] >= datetime.strptime('01/11/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/12/2021','%d/%m/%Y'))]
    mean11 = (mounth11[nameColunm].mean())
    meanlist.append(mean11)
    print(f"Media do Mês 11 : {mean11}")

    return meanlist

def sum_for_months(nameColunm):
    sumslist = []

    mounth06 = table.loc[(table['Data'] >= datetime.strptime('01/06/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/07/2021','%d/%m/%Y'))]
    sum06 =  (mounth06[nameColunm].sum())
    sumslist.append(sum06)
    print(f"Soma do Mês 06 : {sum06}")

    mounth07 = table.loc[(table['Data'] >= datetime.strptime('01/07/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/08/2021','%d/%m/%Y'))]
    sum07 = ( mounth07[nameColunm].sum())
    sumslist.append(sum07)
    print(f"Soma do Mês 07 : {sum07}")

    mounth08 = table.loc[(table['Data'] >= datetime.strptime('01/08/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/09/2021','%d/%m/%Y'))]
    sum08 = ( mounth08[nameColunm].sum())
    sumslist.append(sum08)
    print(f"Soma do Mês 08 : {sum08}")

    mounth09 = table.loc[(table['Data'] >= datetime.strptime('01/09/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/10/2021','%d/%m/%Y'))]
    sum09 = ( mounth09[nameColunm].sum())
    sumslist.append(sum09)
    print(f"Soma do Mês 09 : {sum09}")

    mounth10 = table.loc[(table['Data'] >= datetime.strptime('01/10/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/11/2021','%d/%m/%Y'))]
    sum10 = ( mounth10[nameColunm].sum())
    sumslist.append(sum10)
    print(f"Soma do Mês 10 : {sum10}")

    mounth11 = table.loc[(table['Data'] >= datetime.strptime('01/11/2021','%d/%m/%Y')) & (table['Data'] < datetime.strptime('01/12/2021','%d/%m/%Y'))]
    sum11 = (mounth11[nameColunm].sum())
    sumslist.append(sum11)
    print(f"Soma do Mês 11 : {sum11}")

    return sumslist

means = mean_for_months('Chuva (mm)')
sums = sum_for_months('Chuva (mm)')
labels = ['06/2021','07/2021','08/2021','09/2021','10/2021','11/2021']

def plot_bar_chart(height, labels):
    fig = plt.figure(figsize = (10, 5))
    chartBar = plt.bar(x=labels,height=height,width=0.4,)

    plt.bar_label(chartBar, label_type="edge",fmt="%.02f (mm)")

    plt.yticks(range(0,1))
    plt.xlabel("Meses")
    plt.ylabel("Media das precipitações")
    plt.title("Grafico das medias das precipitações em 6 meses")
    plt.show()

# plot_bar_chart(means,labels)
# plot_bar_chart(sums,labels)
