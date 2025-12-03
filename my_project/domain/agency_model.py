# my_project/domain/agency_model.py (ОСТАННЯ ФІКСАЦІЯ)

from extensions import db

class Agency(db.Model):
    # Назва таблиці у нижньому регістрі (як у Вашій базі)
    __tablename__ = 'agencies'
    
    agency_id = db.Column('agency_id', db.Integer, primary_key=True)
    
    # *** ВИПРАВЛЕНО: Змінено 'name' на 'agency_name' для відповідності MySQL ***
    agency_name = db.Column('agency_name', db.String(255), nullable=False, unique=True)
    
    # Виправлення для інших колонок, які можуть бути іншими (якщо вони використовуються)
    contact_phone = db.Column('contact_phone', db.String(20)) # Приклад виправлення, якщо потрібен
    contact_email = db.Column('contact_email', db.String(255)) # Приклад виправлення, якщо потрібен
    
    # Оскільки у Вашому скріншоті немає колонки 'address', я прибираю її.
    # Якщо 'address' існує, додайте її сюди.

    def to_dict(self):
        return {
            'id': self.agency_id,
            # *** ВИПРАВЛЕНО: В to_dict повертаємо 'name' з agency_name ***
            'name': self.agency_name,
            # У Вашій таблиці є contact_phone та contact_email, додамо їх:
            'contact_phone': self.contact_phone,
            'contact_email': self.contact_email
            # 'address': self.address # Цю колонку прибрано, якщо вона не потрібна
        }