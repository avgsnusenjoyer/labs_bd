# my_project/domain/animator_model.py (ОСТАННЯ ФІКСАЦІЯ)

from extensions import db
from my_project.domain.agency_model import Agency 

# ВИПРАВЛЕНО: Змінено регістр стовпців та назви таблиці у ForeignKey
animator_agency_association = db.Table('animator_agency',
    db.Column('animator_id', db.Integer, db.ForeignKey('animators.animator_id'), primary_key=True),
    db.Column('agency_id', db.Integer, db.ForeignKey('agencies.agency_id'), primary_key=True)
)

class Animator(db.Model):
    # ВИПРАВЛЕНО: Назва таблиці у нижньому регістрі (як у Вашій базі)
    __tablename__ = 'animators'
    
    # ВИПРАВЛЕНО: Назви стовпців у нижньому регістрі (рекомендовано)
    animator_id = db.Column('animator_id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(100), nullable=False)
    last_name = db.Column('last_name', db.String(100), nullable=False)
    phone_number = db.Column('phone_number', db.String(20), unique=True)
    rating = db.Column('rating', db.Numeric(2, 1))
    
    agencies = db.relationship('Agency', secondary=animator_agency_association, backref='animators', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.animator_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'rating': float(self.rating) if self.rating else None,
        }