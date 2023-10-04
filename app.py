# from flask import Flask, request, jsonify, make_response
# from flask_restful import Resource, Api
# # interact with db
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({"greetings" : "Hello world"})


# if __name__ == '__main__':
#     app.run(debug=True)

from api import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
