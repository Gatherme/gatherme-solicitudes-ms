import sqlite3

class Schema:

	def __init__(self):
		self.conn = sqlite3.connect('../data/solicitudes.db') 
		self.create_requests_table()

	def create_requests_table(self):
		query1 = "DROP TABLE IF EXISTS Requests"
		self.conn.execute(query1)
 
		query2 = """
		  CREATE TABLE IF NOT EXISTS "Requests" (
		  id INTEGER PRIMARY KEY,
		  user_origin TEXT,
		  user_destination TEXT,
		  is_accepted boolean DEFAULT False,
		  send_date Date DEFAULT CURRENT_DATE
		);
		"""
		self.conn.execute(query2)



class RequestModel:

	def __init__(self):
		self.conn = sqlite3.connect('../data/solicitudes.db')
		
	def is_created(self, usuario_envia, usuario_recibe):
		query = 'select * from Requests where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		if (len(result.fetchall())==0):
			return False
		else:
			return True
		

	def create(self, usuario_envia, usuario_recibe):
		query = 'insert into Requests (user_origin, user_destination) values ("'+usuario_envia+'","'+usuario_recibe+'")'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido creada.</p>', 201

	def list(self):
		query = 'select * from Requests'
		result = self.conn.execute(query)
		rows = result.fetchall()
		return str(rows)

	def accept(self, usuario_envia, usuario_recibe):
		query = 'update Requests SET is_accepted = "True" where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido aceptada.</p>'
		
	def erase(self, usuario_envia, usuario_recibe):
		query = 'delete from Requests where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido borrada.</p>'
		
		
