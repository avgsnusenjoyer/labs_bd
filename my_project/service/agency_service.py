from my_project.dao.agency_dao import AgencyDAO
from my_project.domain.order_model import Order

class AgencyService:
    def __init__(self):
        self.dao = AgencyDAO()
    
    def get_agency_by_id(self, agency_id):
        agency = self.dao.find_by_id(agency_id)
        return agency.to_dict() if agency else None

    # МЕТОД M:1: Отримати замовлення агенції
    def get_agency_orders(self, agency_id):
        agency = self.dao.find_by_id(agency_id) 
        if agency:
            orders = agency.orders.all()
            return [order.to_dict() for order in orders]
        return None