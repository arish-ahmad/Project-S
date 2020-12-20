import socket
def __get_ip():
    '''This function returns the ip address of connected wifi'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=__get_ip()
print(ip)
s.bind(("192.168.43.104",12345))
s.listen(1)
c,addr=s.accept()
print(f'connected to{addr} and {c}')
f=open('happy.mp4','rb')
data=f.read(4096)
while data:
    c.send(data)
    data=f.read(4096)
f.close()
print('Done sending')
