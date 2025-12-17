from flask import Flask
from extensions import db
from my_project.controller.procedure_controller import proc_bp
app.register_blueprint(proc_bp)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxcv2010@localhost/animator_orders_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        # Імпорт всіх контролерів
        from my_project.controller.animator_controller import animator_bp
        from my_project.controller.agency_controller import agency_bp
        from my_project.controller.procedure_controller import proc_bp
        app.register_blueprint(proc_bp)
        
        # Реєстрація контролерів
        app.register_blueprint(animator_bp)
        app.register_blueprint(agency_bp)
        app.register_blueprint(proc_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)