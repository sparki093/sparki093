from os import replace
from numpy import NaN, double
import pandas as pd

data = pd.read_csv ('world_countries.txt')
frame = pd.DataFrame(data)

def coastline(frame,data) -> None:
    """  число стран без береговой линии и процент таких стран """
    all = len(data['coastline'])
    ctn = 0
    for i in frame['coastline']:
        ch = i.replace(',','.')
        if float(ch)==0:
            ctn+=1
    print(ctn)
    print('Число стран без береговой линии - {0}, их процент от общего - {1}'.format(ctn,ctn/all*100))

def max_min(data) -> None:
    """  Страны с максимальной и минимальной плотностью населения  """
    d = {}
    for i,row in data.iterrows():
        d[row['country']]= row['population']/row['area']
    key_max = max(d,key=d.get)
    key_min = min(d,key=d.get)
    print('Страна {} с максимальной плотностью: {} \nстрана {} с минимально плотность: {}'.format(key_max,d[key_max],key_min,d[key_min]))

def area_phone(data) -> None:
    """ вывести ргион, где меньше всего людей владеют телефонами """
    d = {}
    data['phones_per_1000'] = data['phones_per_1000'].astype('str') #преобразовать в строку иначе ошибка
    data['phones_per_1000'] = data['phones_per_1000'].str.replace(',','.')
    for i,row in data.iterrows():
        d[row['region']] = (row['phones_per_1000'])
    key_min = min(d,key=d.get)
    print("В регионе {} люди меньше всего владеют телефонами".format(key_min))

def literacy(data) -> None:
    """ вывести список стран у которых отсутствует грамотность и население более 1кк """
    data['literacy'] = data['literacy'].astype('str')
    d = data[(data.literacy=='nan') & (data.population>1000000)]
    print(d)

def migration(data):
    """страны в которых преобладает сельское хозяйство над промышленностью и обслуживанием"""

    data['net migration']=data['net migration'].replace(',','.',regex=True).astype('float')
    d = data[(data.agriculture>data.industry) & (data.agriculture>data.service)]
    
    s = d.groupby(by=['country','region'],as_index=False).agg({'net migration':['mean']})
    s['net migration']=s['net migration'].replace(',','.',regex=True).astype('float')
    
    for i,row in s.iterrows():
        if row[2]>0:
            print(row[0])



migration(data)
literacy(data)
coastline(frame,data)
max_min(data)
area_phone(data)

