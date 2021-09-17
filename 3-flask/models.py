from appic import db

class Houses(db.Model):
     house_id = db.Column(db.Integer,primary_key=True, nullable=False)
     latitude = db.Column(db.Float,nullable=False)
     longitude = db.Column(db.Float, nullable=False)
     family_count = db.Column(db.Integer)

     def __repr__(self) -> str:
         return '<House id: {}'.format(self.house_id)