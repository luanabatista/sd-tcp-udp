from io import BufferedReader
import socket

# cria o socket
# especifica o tipo de socket em .AF_INET
# especifica o tipo de protocolo em .SOCK_STREAM (para sockets TCP)
# precisa estar ligado a uma porta para saber se vai receber ou hotear alguma coisa
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
porta = 9999

# diz onde o servidor tem que escutar
server.bind((host, porta))

# é possível limitar o número de conexões não aceitas até rejeitar uma nova
server.listen()
print(f"Servidor escutando em {host}:{porta}")

while True:
    # cria um socket apenas para aceitar comunicação
    # atribui o endereço da conexão que está chegando
    # quando algum cliente tenta se conectar ao servidor
    # o método retorna o endereço do mesmo e o socket que pode ser usado para se comunicar com ele

    # espera até que alguem cliente se conecte
    client, address = server.accept()

    # confirmação da conexão printando o IP
    print(f"Conectado com {address}")

    # espera mensagem do cliente
    # especifica o tamanho do buffer
    # decodifica a mensagem
    nome_arquivo = client.recv(1024).decode('utf-8')

    try:
        # tenta abrir o arquivo
        f = open(nome_arquivo, "rb")
    except OSError:
        # se não conseguir, envia uma mensagem de erro pro cliente
        client.send("Arquivo nao encontado!".encode())
    with f:
        # se conseguir, manda cada linha do arquivo para o cliente
        for line in f:
            client.send(line)

    #sinaliza para o cliente que a transferencia encerrou
    client.send("tchau".encode())
