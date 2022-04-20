#  * Argumentos: <HostIP> <porta> <mensagem>
#  Ex. java Cliente 127.0.0.1 6789 "mensagem teste"
#  O servidor devolve a msg (echo)

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#voce deseja corrigir quantas perguntas
#for

message = str(input("Insira <questão;alternativas;respostas>: "))
client.sendto(message.encode(), ('127.0.0.1', 9999))
recv_msg_bytes, address = client.recvfrom(1024)
recv_msg_string = recv_msg_bytes.decode()

message = str(input("Insira <número da questão>;<número alternativas>;<respostas>: "))
client.sendto(message.encode(), ('127.0.0.1', 9999))
recv_msg_bytes, address = client.recvfrom(1024)
recv_msg_string = recv_msg_bytes.decode()

message = str(input("Insira <número da questão>;<número alternativas>;<respostas>: "))
client.sendto(message.encode(), ('127.0.0.1', 9999))
recv_msg_bytes, address = client.recvfrom(1024)
recv_msg_string = recv_msg_bytes.decode()

message = str(input("Insira <número da questão>;<número alternativas>;<respostas>: "))
client.sendto(message.encode(), ('127.0.0.1', 9999))
recv_msg_bytes, address = client.recvfrom(1024)
recv_msg_string = recv_msg_bytes.decode()

print(recv_msg_string)
client.close()
