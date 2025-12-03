from flask import Flask
from extensions import db

DATABASE_URI = 'mysql+mysqldb://root:zxcv2010@localhost/animator_orders_db'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from my_project.controller.animator_controller import animator_bp
    app.register_blueprint(animator_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)