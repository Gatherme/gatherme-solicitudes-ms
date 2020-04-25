from flask import Flask, request, jsonify
from models import Schema
from service import RequestService

app = Flask(__name__)

@app.route("/<user>/gatherme-requests/create", methods=["POST"])
def create(user):
	return RequestService().create(user, request.get_json())

@app.route("/<user>/gatherme-requests/sent", methods=["GET"])
def listSent(user):
	return jsonify(RequestService().sentList(user))
	
@app.route("/<user>/gatherme-requests/inbox", methods=["GET"])
def listInbox(user):
	return jsonify(RequestService().inboxList(user))

@app.route("/<user>/gatherme-requests/accept", methods=["PUT"])
def accept(user):
	return RequestService().accept(user, request.get_json())
	
@app.route("/<user>/gatherme-requests/reject", methods=["PUT"])
def reject(user):
	return RequestService().reject(user, request.get_json())
	
@app.route("/<user>/gatherme-requests/erase", methods=["DELETE"])
def erase(user):
	return RequestService().erase(user, request.get_json())


if __name__ == "__main__":
	Schema()
	app.run(debug=True, host='0.0.0.0', port=4444)


