import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
questions = 4

for x in range(questions):
    message = str(input(f"Insira sua resposta: "))
    client.sendto(message.encode(), ('127.0.0.1', 9999))

print('Resultado da correção:')
for x in range(questions):
    recv_msg_bytes, address = client.recvfrom(1024)
    recv_msg_string = recv_msg_bytes.decode()
    print(f"{recv_msg_string}")

client.close()