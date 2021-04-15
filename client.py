import socket
s=socket.socket()
s.connect(('192.168.214.174',8584))
conn=True
while conn:
    msg=input('Enter your message: ')
    s.send(msg.encode('utf-8'))
    if msg == 'no':
        conn=False
        s.close()
