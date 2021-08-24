import socket
import threading
from gtts import gTTS
from playsound import  playsound
import os
import time

HEADER = 64
PORT = 5050
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] {msg}")
            elif (msg=="1"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome3.mp3")
            elif (msg=="2"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome6.mp3")
            elif (msg[0]=="1"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                language="hi"
                mytext="आपने कहा  "+ msg[1:]
                myobj=gTTS(text=mytext,lang=language)
                myobj.save("welcome4.mp3")
                playsound("welcome4.mp3")
                playsound("welcome7.mp3")
                os.remove("welcome4.mp3")
            elif (msg[0]=="2"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                language="hi"
                mytext=msg[1:] + "आपके सामने खड़ा है "
                myobj=gTTS(text=mytext,lang=language)
                myobj.save("welcome1.mp3")
                playsound("welcome1.mp3")
                os.remove("welcome1.mp3")
            elif (msg=="00"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome5.mp3")
            elif (msg=="01"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome15.mp3")
                time.sleep(4)
                playsound("welcome8.mp3")
                playsound("welcome2.mp3")
            elif (msg=="unk"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome9.mp3")
                playsound("welcome11.mp3")
            elif (msg=="ocr"):
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome16.mp3")
                playsound("welcome17.mp3")
            else:
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(FORMAT))
                playsound("welcome10.mp3")
                playsound("welcome14.mp3")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    playsound("welcome12.mp3")
    playsound("welcome13.mp3")
    playsound("welcome14.mp3")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()