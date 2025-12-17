from extensions import db
from sqlalchemy import text

class ProcedureDAO:
    @staticmethod
    def call_batch_insert():
        # Викликає процедуру для масової вставки клієнтів
        db.session.execute(text("CALL BatchInsertClients()"))
        db.session.commit()

    @staticmethod
    def get_avg_cost():
        # Викликає процедуру, яка використовує GetAvgCost()
        result = db.session.execute(text("CALL ShowAvgCost()"))
        return result.fetchone()[0]

    @staticmethod
    def call_dynamic_split():
        # Викликає процедуру з курсором для поділу таблиць
        db.session.execute(text("CALL DynamicSplitOrders()"))
        db.session.commit()