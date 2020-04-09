import sqlite3

class Schema:

	def __init__(self):
		self.conn = sqlite3.connect('../data/solicitudes.db') 
		self.create_solicitudes_table()

	def create_solicitudes_table(self):
		query1 = "DROP TABLE IF EXISTS Solicitudes"
		self.conn.execute(query1)
 
		query2 = """
		  CREATE TABLE IF NOT EXISTS "Solicitudes" (
		  id INTEGER PRIMARY KEY,
		  Usuario_envia TEXT,
		  Usuario_recibe TEXT,
		  is_accepted boolean DEFAULT False,
		  fecha_envio Date DEFAULT CURRENT_DATE
		);
		"""
		self.conn.execute(query2)



class SolicitudModel:

	def __init__(self):
		self.conn = sqlite3.connect('../data/solicitudes.db')
		
	def is_created(self, usuario_envia, usuario_recibe):
		query = 'select * from Solicitudes where Usuario_envia = "'+usuario_envia+'" and Usuario_recibe = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		if (len(result.fetchall())==0):
			return False
		else:
			return True
		

	def create(self, usuario_envia, usuario_recibe):
		query = 'insert into Solicitudes (Usuario_envia, Usuario_recibe) values ("'+usuario_envia+'","'+usuario_recibe+'")'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido creada.</p>', 201

	def list(self):
		query = 'select * from Solicitudes'
		result = self.conn.execute(query)
		rows = result.fetchall()
		return str(rows)

	def accept(self, usuario_envia, usuario_recibe):
		query = 'update Solicitudes SET is_accepted = "True" where Usuario_envia = "'+usuario_envia+'" and Usuario_recibe = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido aceptada.</p>'
		
	def erase(self, usuario_envia, usuario_recibe):
		query = 'delete from Solicitudes where Usuario_envia = "'+usuario_envia+'" and Usuario_recibe = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido borrada.</p>'
		
		
