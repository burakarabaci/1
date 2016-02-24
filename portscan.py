import socket

host = 'localhost'
port = 49155
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def pscan(port):
    try:
        s.connect((host,port))
        return True
    except:
        return False
    
for x in range(49150,49170):
    if pscan(x):
        print('Port',x,'is open !!!')
    else:
        print('Port',x,'is closed')
