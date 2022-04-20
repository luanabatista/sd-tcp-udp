import socket

# cria o socket do tipo SOCK_STREAM (TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tenta se conectar com 127.0.0.1:9999
client.connect(('127.0.0.1', 9999))

# solicita pro usuario o nome do arquivo
# envia pro servidor o nome do arquivo
client.send(input("Digite o nome do arquivo: ").encode('utf-8'))

# espera a primeira resposta do servidor
res = client.recv(1024)

# verifica se o arquivo não foi encontrado
if res == b'Arquivo nao encontado!': 
    # se sim, printa pro usuario a mensagem e encerra o programa
    print(res.decode())
    exit(0)

# printa o conteúdo do arquivo
while res != b"tchau":
    print(res.decode())
    res = client.recv(1024)

# encerra a conexão
client.shutdown(0)