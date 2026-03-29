from flask import Flask
from routes.userRoutes import user_api
from routes.contactRoutes import contact_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_api)
app.register_blueprint(contact_api)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
