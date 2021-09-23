from appic import app,db
from flask import render_template,request,jsonify
from models import Houses

@app.route('/post',methods=["POST"])
def index():
    """ API для оновления или вставки новой записи в бд по по id  """
    if request.method == 'POST':
        data = request.get_json()
        for i in data:
            print(i)
            ses = db.session.query(Houses).filter_by(house_id=i['id']).first()
            if ses:
                ses.latitude=i['latitude']
                ses.longitude=i['longitude']
                ses.family_count=i['family_count']
            else:
                db.session.add(Houses(latitude=i['latitude'],
                            longitude=i['longitude'],family_count=i['family_count']))
            db.session.commit()
    return jsonify({'suc':'100'})

@app.route('/')
def id():
    house = Houses.query.all()
    return render_template('index.html',house = house)