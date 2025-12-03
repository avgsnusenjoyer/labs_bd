from my_project.dao.animator_dao import AnimatorDAO

class AnimatorService:
    def __init__(self):
        self.dao = AnimatorDAO()

    def get_all_animators(self):
        animators = self.dao.find_all()
        return [animator.to_dict() for animator in animators]

    def get_animator_by_id(self, animator_id):
        animator = self.dao.find_by_id(animator_id)
        return animator.to_dict() if animator else None
    
    def create_animator(self, data):
        rating = data.get('rating')
        if rating is not None and (rating < 0 or rating > 5.0):
            raise ValueError("Рейтинг має бути в межах від 0.0 до 5.0.")
        
        new_animator = self.dao.create(data)
        return new_animator.to_dict()
    
    def update_animator(self, animator_id, data):
        updated_animator = self.dao.update(animator_id, data)
        return updated_animator.to_dict() if updated_animator else None

    def delete_animator(self, animator_id):
        return self.dao.delete(animator_id)
    
    def get_animator_agencies(self, animator_id):
        animator = self.dao.find_by_id(animator_id)
        if animator:
            agencies = animator.agencies.all()
            return [agency.to_dict() for agency in agencies]
        return None