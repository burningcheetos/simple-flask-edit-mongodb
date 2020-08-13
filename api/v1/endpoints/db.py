from flask import request
from flask_restplus import Resource, reqparse
from api.v1.restplus import api
from api.v1.data import db
import json


ns = api.namespace('v1/db', description="just a db endpoint")


parser = reqparse.RequestParser()
parser.add_argument('entry', type=int, help='Which entry to pull')

data = reqparse.RequestParser()
data.add_argument('user_data', type=dict, help='user entry')

@ns.route('/')
class UpdateDB(Resource):

    @api.expect(parser)
    def get(self):
        """Get Data"""
        try:
            arg = int(request.args['entry'])
        except TypeError:
            return "Must use numbers", 400
        if -1 == arg:
            return db, 200
        if arg < -1:
            return "Error", 400

        try:
            user_entry = list(filter(lambda x: x['id'] == arg, db))[0]
        except IndexError:
            return "No user entry", 500
        return user_entry, 200

    @api.expect(parser, data)
    def put(self):
        try:
            arg = int(request.args['entry'])
        except TypeError:
            return "Must use numbers", 400
        if -1 == arg:
            return db, 200
        if arg < -1:
            return "Error", 400

        try:
            db[arg]
        except IndexError:
            return "No user entry", 500

        user_data = json.loads(request.args['user_data'])
        for user in db:
            if user['id'] == arg:
                user.update(user_data)