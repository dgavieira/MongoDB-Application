# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.doc_csv import Csv
from api.errors import forbidden

class CsvsApi(Resource):
    """
        Flask-resftul resource for returning db.meal collection.

        :Example:

        >>> from flask import Flask
        >>> from flask_restful import Api
        >>> from app import default_config

        # Create flask app, config, and resftul api, then add MealsApi route
        >>> app = Flask(__name__)
        >>> app.config.update(default_config)
        >>> api = Api(app=app)
        >>> api.add_resource(MealsApi, '/meal/')

    """

    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all documents in meal collection.
        JSON Web Token is required.

        :return: JSON object
        """
        output = Csv.objects()
        return jsonify({'result': output})

    @jwt_required
    def post(self) -> Response:
        """
        POST response method for creating meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        authorized: bool = Csv.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Csv(**data).save()
            output = {'id': str(post_user.id)}
            return jsonify({'result': output})
        else:
            return forbidden()

class CsvApi(Resource):
    """
        Flask-resftul resource for returning db.meal collection.

        :Example:

        >>> from flask import Flask
        >>> from flask_restful import Api
        >>> from app import default_config

        # Create flask app, config, and resftul api, then add MealApi route
        >>> app = Flask(__name__)
        >>> app.config.update(default_config)
        >>> api = Api(app=app)
        >>> api.add_resource(CsvApi, '/csv/<csv_id>')
    """

    @jwt_required
    def get(self, csv_id: str) -> Response:
        """
        GET response method for single documents in meal collection.

        :return: JSON object
        """
        output = Csv.objects.get(id=csv_id)
        return jsonify({'result': output})

    @jwt_required
    def put(self, csv_id: str) -> Response:
        """
        PUT response method for updating a meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        data = request.get_json()
        put_user = Csv.objects(id=csv_id).update(**data)
        return jsonify({'result': put_user})

    @jwt_required
    def delete(self, user_id: str) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)

        :return: JSON object
        """
        authorized: bool = Csv.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Csv.objects(id=user_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()