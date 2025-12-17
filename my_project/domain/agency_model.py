from extensions import db

class Agency(db.Model):
    __tablename__ = 'agencies'
    
    agency_id = db.Column('agency_id', db.Integer, primary_key=True)
    agency_name = db.Column('agency_name', db.String(255), nullable=False)
    contact_phone = db.Column('contact_phone', db.String(20))
    contact_email = db.Column('contact_email', db.String(255))

    # Зв'язок 1:M (Агентство має багато замовлень)
    orders = db.relationship('Order', backref='agency_ref', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.agency_id,
            'name': self.agency_name,
            'phone': self.contact_phone,
            'email': self.contact_email
        }