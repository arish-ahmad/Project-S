import socket
def get_ip():
    ip= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8", 80))
    return ip.getsockname()[0]
    s.close()
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = str(get_ip())
print(host)
port = 8584
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
