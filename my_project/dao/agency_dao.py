from extensions import db
from my_project.domain.agency_model import Agency

class AgencyDAO:
    def find_all(self):
        return db.session.execute(db.select(Agency)).scalars().all()

    def find_by_id(self, agency_id):
        return db.session.get(Agency, agency_id)

    # Додайте тут інші методи CRUD, якщо вони потрібні