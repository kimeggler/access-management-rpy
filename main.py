from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

api_secret = "6O3Gur1qXijWvTsXcKLI5ohLRxEYb5iC"

put_args = reqparse.RequestParser()
put_args.add_argument("secret", type=str, help="The secret is required to unlock the door", required=True)

badge_post_args = reqparse.RequestParser()
badge_post_args.add_argument("secret", type=str, help="The secret is required to unlock the door", required=True)
badge_post_args.add_argument("data", type=str, help="The secret is required to unlock the door", required=True)


def reject_if_invalid(secret):
    if secret != api_secret:
        abort()

class Open(Resource):
    def put(self):
        return "opened" 


class Write(Resource):
    def put(self):
        return "waiting for badge..."


class Delete(Resource):
    def put(self):
        return "waiting for badge to clear data..."


api.add_resource(Open, "/open")
api.add_resource(Open, "/write")
api.add_resource(Open, "/delete")


if  __name__ == "__main__":
    app.run(debug=True)