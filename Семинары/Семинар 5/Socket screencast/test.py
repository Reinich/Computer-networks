import socket
import threading
from time import sleep

ya_sock = socket.socket() # создаем сокет 
ya_adr = ("87.250.250.242", 443) # указывает в массиве ip адрес и порт
ya_sock.connect(ya_adr) # создаем подключение

data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n" # отправляем запрос в байтах
ya_sock.send(data_out)

# data_in = ya_sock.recv(1024) # сохраняем в переменную ответ от я.ру
# print(data_in) # вывод будет коротким - поскольку пакеты приходят постепенно

data_in = b""
def recieving():
    global data_in
    while True:
        data_chunk = ya_sock.recv(1024)
        data_in = data_in + data_chunk
rec_thread = threading.Thread(target=recieving)
rec_thread.start()
sleep(4)
print(data_in)
ya_sock.close()