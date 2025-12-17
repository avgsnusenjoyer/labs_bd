from extensions import db
from my_project.domain.animator_model import Animator

class AnimatorDAO:
    def find_all(self):
        # Повертає список всіх об'єктів Animator
        return db.session.execute(db.select(Animator)).scalars().all()

    def find_by_id(self, animator_id):
        # Повертає об'єкт Animator за первинним ключем (ID)
        return db.session.get(Animator, animator_id)
    
    def create(self, data):
        # Створює та зберігає новий об'єкт Animator
        new_animator = Animator(**data)
        db.session.add(new_animator)
        db.session.commit()
        return new_animator

    def update(self, animator_id, data):
        # Оновлює об'єкт Animator за ID
        animator = self.find_by_id(animator_id)
        if animator:
            for key, value in data.items():
                setattr(animator, key, value)
            db.session.commit()
            return animator
        return None

    def delete(self, animator_id):
        # Видаляє об'єкт Animator за ID
        animator = self.find_by_id(animator_id)
        if animator:
            db.session.delete(animator)
            db.session.commit()
            return True
        return False