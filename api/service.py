from models import RequestModel

class RequestService:

	def __init__(self):
		self.model = RequestModel()

	def create(self, params):
		if params['user_origin'] == params['user_destination']:
			return '<p>Imposible crear. Usuario destino es igual a usuario origen.</p>', 400
		elif self.model.is_created(params['user_origin'], params['user_destination']):
			return '<p>Imposible crear. La solicitud de GATHER ya existe.</p>', 400
		else: return self.model.create(params['user_origin'], params['user_destination'])

	def list(self):
		return self.model.list()

	def accept(self, params):
		if self.model.is_created(params['user_origin'], params['user_destination']):
			return self.model.accept(params['user_origin'], params['user_destination'])
		else: return '<p>Parametros no validos.</p>', 400
		
	def erase(self, params):
		if self.model.is_created(params['user_origin'], params['user_destination']):
			return self.model.erase(params['user_origin'], params['user_destination'])
		else: return '<p>Parametros no validos.</p>', 400
