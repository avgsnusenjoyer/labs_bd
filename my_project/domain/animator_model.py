from extensions import db

class Animator(db.Model):
    __tablename__ = 'animators'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))

    # ВИПРАВЛЕНО: посилання на клас AnimatorOrderParticipation для усунення InvalidRequestError
    orders = db.relationship('Order', secondary='animator_order_participation', backref='animators_list')

    def to_dict(self):
        return {
            'id': self.id,
            'name': f"{self.first_name} {self.last_name}",
            'phone': self.phone
        }