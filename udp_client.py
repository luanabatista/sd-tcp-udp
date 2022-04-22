#  * Argumentos: <HostIP> <porta> <mensagem>
#  Ex. java Cliente 127.0.0.1 6789 "mensagem teste"
#  O servidor devolve a msg (echo)

import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

questions = 4
#voce deseja corrigir quantas perguntas
#for

for x in range(questions):
    message = str(input(f"Resposta {x+1}:"))
    client.sendto(message.encode(), ('127.0.0.1', 9999))

for x in range(questions):
    recv_msg_bytes, address = client.recvfrom(1024)
    recv_msg_string = recv_msg_bytes.decode()
    print(recv_msg_string)

client.close()
