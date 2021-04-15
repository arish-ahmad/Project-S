import socket
s=socket.socket()
s.connect(('192.168.214.174',8584))
msg='Hello connection is established'
s.send(msg.encode('utf-8'))
s.close()