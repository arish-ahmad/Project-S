import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 2525
s.bind((host,port))
s.listen(4)
print(host)
print('server is ready to accept connection')
clientobject,add=s.accept()
print('connected with this address',add)
while True:
   gotmsg=clientobject.recv(1024)
   gotmsg.decode('utf-8')
   print(gotmsg)
   if gotmsg ==  'q':
      s.close()
#s.close()