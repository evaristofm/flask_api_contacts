from flask_restful import Resource, marshal
from app.models import User
from app.schemas import user_field
from app import db, requests
import jwt
import datetime
from flask import current_app

class Login(Resource):
    def post(self):
        payload = requests.only(["username", "password"])

        username = payload["username"]
        password = payload["password"]

        user = User.query.filter_by(username=username).first()

        if not user and not user.compare_password(password):
            return {"message": "Credenciais Inválidas!"}, 404

        data = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }

        token = jwt.encode(data, current_app.config["SECRET_KEY"])

        return {"acess_token": token.decode("utf-8")}

class Register(Resource):
    def post(self):
        payload = requests.only(["username", "password"])

        username = payload["username"]
        password = payload["password"]

        user = User(username, password)

        db.session.add(user)
        db.session.commit()

        return marshal(user, user_field, "user")