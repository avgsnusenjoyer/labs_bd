from extensions import db

class AnimatorOrderParticipation(db.Model):
    __tablename__ = 'animator_order_participation'
    
    animator_id = db.Column(db.Integer, db.ForeignKey('animators.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), primary_key=True)
    performance_role = db.Column(db.String(100))
    animator_fee = db.Column(db.Numeric(8, 2))
    
    # Додаткові поля (Payload)
    performance_role = db.Column('performance_role', db.String(100))
    animator_fee = db.Column('animator_fee', db.Numeric(10, 2))
    
    # Зв'язки до основних моделей
    animator = db.relationship('Animator', backref=db.backref('order_participations', lazy="dynamic"))
    order = db.relationship('Order', backref=db.backref('animator_participations', lazy="dynamic"))

    def to_dict(self):
        return {
            'animator_id': self.animator_id,
            'order_id': self.order_id,
            'performance_role': self.performance_role,
            'animator_fee': float(self.animator_fee) if self.animator_fee else None,
        }