import socket
from PIL import Image
import io
import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 33333))
server_socket.listen(5)



while True:
    client_socket, addr = server_socket.accept()
    im = Image.open('1test.png')
    im_resize = im.resize((500, 500))
    buf = io.BytesIO()
    im.save(buf, format='PNG')
    byte_im = buf.getvalue()
    print(len(byte_im))
    client_socket.send(byte_im)
    
client_socket.close()        
server_socket.close()
