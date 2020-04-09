from flask import Flask, request, jsonify
from models import Schema
from service import SolicitudService

app = Flask(__name__)

@app.route("/solicitudes", methods=["POST"])
def createSol():
	return SolicitudService().create(request.get_json())

@app.route("/solicitudes", methods=["GET"])
def listSol():
	return jsonify(SolicitudService().list())

@app.route("/solicitudes", methods=["PUT"])
def acceptSol():
	return SolicitudService().accept(request.get_json())
	
@app.route("/solicitudes", methods=["DELETE"])
def eraseSol():
	return SolicitudService().erase(request.get_json())


if __name__ == "__main__":
	Schema()
	app.run(debug=True)
