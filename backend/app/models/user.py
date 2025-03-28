from bson import ObjectId
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, email, password=None, _id=None):
        self._id = _id or ObjectId()
        self.email = email
        self.password_hash = generate_password_hash(password) if password else None

    @staticmethod
    def find_by_email(email):
        user_data = current_app.db.users.find_one({"email": email})
        if user_data:
            return User(
                email=user_data['email'],
                _id=user_data['_id']
            )
        return None

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        user_data = {
            "email": self.email,
            "password": self.password_hash
        }
        if not self._id:
            result = current_app.db.users.insert_one(user_data)
            self._id = result.inserted_id
        else:
            current_app.db.users.update_one(
                {"_id": self._id},
                {"$set": user_data}
            )
        return self

    def to_dict(self):
        return {
            "_id": str(self._id),
            "email": self.email
        }
















