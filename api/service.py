from models import SolicitudModel

class SolicitudService:

	def __init__(self):
		self.model = SolicitudModel()

	def create(self, params):
		if not self.model.is_created(params['usuario_envia'], params['usuario_recibe']):
			return self.model.create(params['usuario_envia'], params['usuario_recibe'])
		else: return '<p>Imposible crear. La solicitud ya existe.</p>', 400

	def list(self):
		return self.model.list()

	def accept(self, params):
		if self.model.is_created(params['usuario_envia'], params['usuario_recibe']):
			return self.model.accept(params['usuario_envia'], params['usuario_recibe'])
		else: return '<p>Parametros no validos.</p>', 400
		
	def erase(self, params):
		if self.model.is_created(params['usuario_envia'], params['usuario_recibe']):
			return self.model.erase(params['usuario_envia'], params['usuario_recibe'])
		else: return '<p>Parametros no validos.</p>', 400
