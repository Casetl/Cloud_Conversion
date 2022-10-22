from api import create_app
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from api.modelos import db, User, File
from api.modelos import FileSchema, UserSchema
from api.vistas import VistaUser, VistaUsers, VistaSignIn, VistaLogIn


app = create_app()
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors=CORS(app)

api = Api(app)
api.add_resource(VistaUsers, '/users')
api.add_resource(VistaUser, '/user/<int:id_user>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

