
import timeit



code_to_test = """
from PIL import Image
CHUNK_SIZE = 8 * 1024
import io
import socket
sock = socket.socket()
sock.connect(('localhost', 33333))
test = []
current_size = 0
size = 503032
buffer = b''
while current_size != size:
    data = sock.recv(CHUNK_SIZE)

    buffer +=data
  

    current_size += len(buffer)
    print(len(buffer), size)
    if len(buffer) == size:
        print("working")
        break
   



byte_im = buffer
print(len(byte_im))
stream = io.BytesIO(byte_im)
img = Image.open(stream)

img.save("a_test.png")

print("Done")
sock.close()
"""
elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time, "elapsed")