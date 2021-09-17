import json
from shapely.geometry import Polygon,MultiPolygon

with open('us-state.json','r') as read_file:
    data = json.load(read_file) # загрузить json


sp = []
for i in data:
    ''' Проверить входной на type и в зависимости от него построить объект 
        долее сохданный объект добавить в список'''
    a = i['fields']
    
    if a['st_asgeojson']['type'] == 'Polygon':
        poly= Polygon(a['st_asgeojson']['coordinates'][0])
        sp.append({a['name']:poly})

    elif a['st_asgeojson']['type'] == 'MultiPolygon':
        multyP = MultiPolygon(a['st_asgeojson']['coordinates'][0],a['st_asgeojson']['coordinates'][1])
        sp.append({a['name']:multyP})


state = []
with open('file.txt','w') as file:
    file.write('Штаты, которые граничат: \n\n')
    for i in sp:
        for j in i:
        
            for k in sp[1:]:
                for m in k:
                    if i[j].intersects(k[m]):
                        st = j+' - ' + m
                        state.append(st)
                        file.write(st)
                        file.write('\n')
        file.write('\n')