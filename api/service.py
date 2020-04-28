from models import RequestModel

class RequestService:

	def __init__(self):
		self.model = RequestModel()
		self.variables = ['id','user_origin','user_destination','send_date','status']

	def create(self, user_origin, params):
		if user_origin == params['user_destination']:
			return '<p>Imposible crear. Usuario destino es igual a usuario origen.</p>', 400
		elif self.model.is_created(user_origin, params['user_destination']):
			return '<p>Imposible crear. La solicitud de GATHER ya existe.</p>', 400
		else: return self.model.create(user_origin, params['user_destination'])

	def sentList(self, user_origin):
		jsonarray = []
		rows = self.model.list('sent', user_origin)
		for row in rows:
			jsonarray.append( dict(zip(self.variables, row)) )
		return jsonarray
		
	def inboxList(self, user_destination):
		jsonarray = []
		rows = self.model.list('inbox', user_destination)
		for row in rows:
			jsonarray.append( dict(zip(self.variables, row)) )
		return jsonarray

	def accept(self, user_destination, params):
		if self.model.is_created(params['user_origin'], user_destination):
			return self.model.accept(params['user_origin'], user_destination)
		else: return '<p>Parametros no validos.</p>', 400
		
	def reject(self, user_destination, params):
		if self.model.is_created(params['user_origin'], user_destination):
			return self.model.reject(params['user_origin'], user_destination)
		else: return '<p>Parametros no validos.</p>', 400
		
	def erase(self, user_origin, params):
		if self.model.is_created(user_origin, params['user_destination']):
			return self.model.erase(user_origin, params['user_destination'])
		else: return '<p>Parametros no validos.</p>', 400
		
