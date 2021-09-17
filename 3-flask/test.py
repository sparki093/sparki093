import json
import requests
import random


""" ля тетирования апи необходимо запустить main.py. В отдльнов терминале запустить test.py.
        Далее тестирование можно изменять значения словаря data и смотреть ответ по id 
        на странице   'http://127.0.0.1:5000/'  """


def post_add(json):
    r = requests.post('http://localhost:5000/post',json = json)



def add() -> None:
    """Сформировать новые записи
    первый раз записи создадуться, при повторном вызове обновятся значения"""
    for i in range(1,10):
        data = {"id":i,"latitude":round(random.uniform(0,70),2),"longitude":round(random.uniform(0,70),2),
                                 "family_count":random.randint(1,5)}
        post_add(data)

add()
        