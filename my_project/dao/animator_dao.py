from extensions import db
from my_project.domain.animator_model import Animator

class AnimatorDAO:
    def find_all(self):
        return Animator.query.all()

    def find_by_id(self, animator_id):
        return Animator.query.get(animator_id)

    def create(self, data):
        new_animator = Animator(**data)
        db.session.add(new_animator)
        db.session.commit()
        return new_animator

    def update(self, animator_id, data):
        animator = self.find_by_id(animator_id) 
        if animator:
            for key, value in data.items():
                if hasattr(Animator, key): 
                    setattr(animator, key, value)
            db.session.commit()
            return animator
        return None

    def delete(self, animator_id):
        animator = self.find_by_id(animator_id)
        if animator:
            db.session.delete(animator)
            db.session.commit()
            return True
        return False