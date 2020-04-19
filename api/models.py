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
		  send_date Date DEFAULT CURRENT_DATE,
		  status TEXT DEFAULT "sent"
		);
		"""
		self.conn.execute(query2)



class RequestModel:

	def __init__(self):
		self.conn = sqlite3.connect('../data/solicitudes.db')
		
	def is_created(self, usuario_envia, usuario_recibe):
		query = 'select * from Requests where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		return (len(result.fetchall())!=0)
		

	def create(self, usuario_envia, usuario_recibe):
		query = 'insert into Requests (user_origin, user_destination) values ("'+usuario_envia+'","'+usuario_recibe+'")'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido creada.</p>', 201
		

	def list(self, p, user):
		if p == 'sent':
			query = 'select * from Requests where user_origin = "'+user+'"'
			result = self.conn.execute(query)
			rows = result.fetchall()
			return str(rows)
		elif p == 'inbox':
			query = 'select * from Requests where user_destination = "'+user+'"'
			result = self.conn.execute(query)
			rows = result.fetchall()
			return str(rows)


	def accept(self, usuario_envia, usuario_recibe):
		query = 'update Requests SET status = "accepted" where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'" and status = "sent"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido aceptada.</p>'
		
		
	def reject(self, usuario_envia, usuario_recibe):
		query = 'update Requests SET status = "rejected" where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'" and status = "sent"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido rechazada.</p>'
		
		
	def erase(self, usuario_envia, usuario_recibe):
		query = 'delete from Requests where user_origin = "'+usuario_envia+'" and user_destination = "'+usuario_recibe+'"'
		result = self.conn.execute(query)
		self.conn.commit()
		return '<p>La solicitud ha sido borrada.</p>'		
		
