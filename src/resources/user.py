from flask_restful import Resource
from flask_restful import reqparse

from models.user import UserModel


class UserRegister(Resource):

    # Define request parser
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': f"A user with name '{data['username']}' already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {"message": f"User with name '{data['username']}' created succesfully."}, 201
