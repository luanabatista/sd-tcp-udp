import socket

class Question:
    def __init__(self, question, alternatives, answer):
        self.question = question
        self.alternatives = alternatives
        self.answer = answer
class ClientRequest:
    def __init__(self, address, message):
        self.address = address
        self.message = message

# Cria um Socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))

requests = []
questions = []

# Preenche o array com as questões e o gabarito
questions.append(Question(1, 4, 'VVVF'))
questions.append(Question(2, 4, 'VFVF'))
questions.append(Question(3, 4, 'FFVV'))
questions.append(Question(4, 4, 'VFVV'))

# Função que recebe o endereço e processa todos os requests deste endereço
def handle(address):
     
    for client_request in requests: 
        try:
            if client_request.address == address:
                # Pega a mensagem do usuário e a atribui em cada uma das variaveis
                number = int(client_request.message[0]) 
                alternatives = int(client_request.message[1])
                answer = str(client_request.message[2])

                # Para cada questão no array de questões uma resposta do usuário é lida e corrigida
                for question in questions:
                    counter = 0
                    sucesses = 0
                    errors = 0

                    # Compara o número enviado pelo usuário com o número da questão para saber com qual gabarito comparar
                    if question.question == number:

                        for alternative in question.answer:
                            # Compara a resposta com o gabarito
                            if alternative == answer[counter]: # Se for correta incrementa a variável sucesses
                                sucesses += 1

                            else: # Se for incorreta incrementa a variável errors
                                errors += 1
                            counter += 1      
                        server.sendto(f'Questão: {number}; Acertos: {sucesses}; Erros:{errors}'.encode('utf-8'), address)

        except: # Caso não seja possivel corrigir retorna erro para o servidor e para o cliente
            print(f'Erro ao processar request recebido de: {address}')
            server.sendto(f"Erro ao processar requisição {message}".encode('utf-8'), address)

# Função que conta quantas requisições de um determinado cliente existe no array requests
def count_client_requests(address):
    counter = 0
    for client_request in requests: 
        if client_request.address == address:
            counter += 1 
    return counter

# Servidor escutando 
print("Aguardando requisição...")
while True:
    client_message, address = server.recvfrom(1024)
    print(f"Requisição recebida de: {str(address)}")
    message = client_message.decode().split(";")
    requests.append(ClientRequest(address, message))

    # Se houver 4 itens (quant de questoes no array de questoes) executa a função handle
    if count_client_requests(address) == len(questions):
        handle(address)
        