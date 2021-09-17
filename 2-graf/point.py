import networkx as nx
import matplotlib.pyplot as plt
import random


"""  В результате выполнения сформируется 2 фала: 1) картинка графа,
    2) file.txt описание объектов и растояние между ними """


class Point():
    
    def __init__(self,x:float=0) -> None:
        self._x = x
    
    
    def getX(self)-> float:
        return self._x
    
    def distance(self,other):
        dx = self._x - other.getX()
        return dx
    
    def dict(self):
        sp = []
        for s in self.__dict__:
            sp.append({s:self.__dict__[s]})
        return sp

    def __repr__(self) -> str:
        return '{}'.format(self._x)
    
    def __str__(self) -> str:
        return '{}'.format(self._x)


class House(Point):
    
    def __init__(self, x:float, floor:int) -> None:
        self.__floor = floor
        super().__init__(x=x)

    def getFloor(self) -> float:
        return self.__floor


class Parking(House):
    
    def __init__(self, x: float, floor: int,count_place:int) -> None:
        self._count_place = count_place
        super().__init__(x=x, floor=floor)

    def ctn_place(self) ->int:
        """ получить количество мест на парковке """
        return self._count_place



#Сгенерировать объекты

p1 = Point(round(random.uniform(5,20),2))
p2 = Point(round(random.uniform(5,40),2))
h1 = House(round(random.uniform(5,40),2),random.randint(1,10))
pa1 = Parking(round(random.uniform(5,40),2),random.randint(1,10),random.randint(100,1000))
p3 = Point(round(random.uniform(5,20),2))
p4 = Point(round(random.uniform(5,40),2))
h3 = House(round(random.uniform(5,40),2),random.randint(1,10))
pa2 = Parking(round(random.uniform(5,40),2),random.randint(1,10),random.randint(100,1000))
pa3 = Parking(round(random.uniform(5,40),2),random.randint(1,10),random.randint(100,1000))
h7 = House(round(random.uniform(5,40),2),random.randint(1,10))

nodes = [(p1,p2,round(p2.distance(p1),2)),
         (p2,h1,round(h1.distance(p2),2)),
         (p3,p2,round(p2.distance(p3),2)),
         (p3,pa1,round(pa1.distance(p3),2)),
         (pa1,p4,round(p4.distance(pa1),2)),
         (p4,h1,round(h1.distance(p4),2)),
         (p4,h3,round(h3.distance(p4),2)),
         (h3,pa2,round(pa2.distance(h3),2)),
         (p2,h1,round(h1.distance(p2),2)),
         (pa2,h7,round(h7.distance(pa2),2)),
         (h7,p1,round(p1.distance(h7),2))]


graph = nx.DiGraph() # создание ориентированного графа

#добавить вершины и веса
for i in nodes:
    graph.add_edge(i[0],i[1],weight=i[2])



#список всех весов ребер
weight = nx.get_edge_attributes(graph,'weight')
#position
pos = nx.circular_layout(graph)
#рисуем вес ребра
nx.draw_networkx_edge_labels(graph,pos,edge_labels=weight)


nx.draw_circular(graph,node_color='red',
                        node_size=1000,
                        with_labels=True)
plt.savefig('file.png') # сохранить граф с весами



#расчет кратчайших путей для всех пар вершин
predecessor, _ = nx.floyd_warshall_predecessor_and_distance(graph)




with open('file.txt','+a') as f:

    for i in predecessor:
        for j in predecessor:
                
            try:
                #кратчайший путь
                shortes_a_d = nx.reconstruct_path(i,j,predecessor)
                

                #список ребер кратчайшего пути
                edges = [(a,b) for a,b in zip(shortes_a_d,shortes_a_d[1:])]
                sum = 0
                for k in edges:
                    q = k[1].getX()-k[0].getX()
                    sum+=q
            
                f.write('< Объект {} атрибуты({}) > - < Объект {} атрибуты({})> : список вершин - {}, длина: {}>'.format(i,i.dict(),j,j.dict(),
                                                                                    shortes_a_d,sum))
                f.write("\n")
            except Exception:
                pass
        f.write('***********')
        f.write("\n")

    

