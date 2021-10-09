import socket

host = ''
port = 5560

storedValue = "Words, and stuff!"

def setupServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created");
	try:
		s.bind((host, port))
	except socket.error as msg:
		print(msg)
	print("Socket bind complete")
	return s
	
def setupConnection():
	s.listen(1)
	conn, address = s.accept()
	print("Connected to: " + address[0] + ":" + str(address[1]))
	return conn

def GET():
	reply = storedValue
	return reply
	
def REPEAT(dataMessage):
	reply = dataMessage[1]
	return reply
	
def dataTransfer():
	while True:
		data = conn.recv(1024)
		data = data.decode('utf-8')
		dataMessage = data.split(' ', 1)
		command = dataMessage[0]
		if command == 'GET':
			reply = GET()
		elif command == 'REPEAT':
			reply = REPEAT(dataMessage)
		elif command == 'EXIT':
			print("Client Left")
			break
		elif command == 'KILL':
			print("Server shutting down")
			s.close()
			break
		else:
			reply = "Unknown command"
			
		conn.sendall(str.encode(reply))
		print("Data sent")
	conn.close()
	
s = setupServer()

while True:
	try:
		conn = setupConnection()
		dataTransfer(conn)
	except:
		break
