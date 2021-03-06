import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
HOST = '0.tcp.ngrok.io'  # The server's hostname or IP address
PORT = 16176    
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



while True:
    print("[ 1 ] for face recognition")
    print("[ 2 ] for detection")
    print("[ 1(name) ] to speak name")
    print("[ 2(name) ] to speak name of person standing in front of you")
    print("[ unk ] to tell unknown is standing")
    print("[ ocr ] to tell text is detected")
    s=str(input("Enter value 1 or 2: "))
    send(s)
    
send(DISCONNECT_MESSAGE)  