from appic import app,db
from flask import render_template,request,jsonify
from models import Houses

@app.route('/post',methods=["POST"])
def index():
    """ API для оновления или вставки новой записи в бд по по id  """
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        ses = db.session.query(Houses).filter_by(house_id=data['id']).first()
        if ses:
            ses.latitude=data['latitude']
            ses.longitude=data['longitude']
            ses.family_count=data['family_count']
        else:
            db.session.add(Houses(latitude=data['latitude'],
                            longitude=data['longitude'],family_count=data['family_count']))
        db.session.commit()
    return jsonify({'suc':'100'})

@app.route('/')
def id():
    house = Houses.query.all()
    return render_template('index.html',house = house)