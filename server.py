import socket
def get_ip():
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(('8.8.8.8',80))
   return s.getsockname()[0]
host = str(get_ip())
port = 8584
print(host)
s.bind((host,port))
s.listen(4)
print(host)
print('server is ready to accept connection')
clientobject,add=s.accept()
print('connected with this address',add)
conn=True
while conn:
   gotmsg=clientobject.recv(1024)
   gotmsg.decode('utf-8')
   print(gotmsg)
   if len(gotmsg) == 0:
      conn=False
      s.close()
