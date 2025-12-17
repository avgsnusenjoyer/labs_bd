from extensions import db

class Order(db.Model):
    __tablename__ = 'orders'
    
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False)
    order_address = db.Column(db.String(255))
    total_cost = db.Column(db.Numeric(10, 2))
    client_id = db.Column(db.Integer)
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.agency_id'))
    
    # НОВЕ ПОЛЕ: для синхронізації з тригером у MySQL
    event_type_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'order_date': str(self.order_date),
            'total_cost': float(self.total_cost) if self.total_cost else 0,
            'agency_id': self.agency_id,
            'event_type_id': self.event_type_id
        }