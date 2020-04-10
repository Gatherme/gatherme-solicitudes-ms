from flask import Flask, request, jsonify
from models import Schema
from service import RequestService

app = Flask(__name__)

@app.route("/requests", methods=["POST"])
def createSol():
	return RequestService().create(request.get_json())

@app.route("/requests", methods=["GET"])
def listSol():
	return jsonify(RequestService().list())

@app.route("/requests", methods=["PUT"])
def acceptSol():
	return RequestService().accept(request.get_json())
	
@app.route("/requests", methods=["DELETE"])
def eraseSol():
	return RequestService().erase(request.get_json())


if __name__ == "__main__":
	Schema()
	app.run(debug=True)


