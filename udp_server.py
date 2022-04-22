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
print("Aguardando requisição...")

requests = []
connected_clients = []
questions = []
user_questions = []
user_results = []

question1 = Question(1, 4, 'VVVF')
questions.append(question1)
question2 = Question(2, 4, 'VFVF')
questions.append(question2)
question3 = Question(3, 4, 'FFVV')
questions.append(question3)
question4 = Question(4, 4, 'VFVV')
questions.append(question4)


def handle(address):
    for client_request in requests: 
        if client_request.address == address:
            number = int(client_request.message[0])
            alternatives = int(client_request.message[1])
            answer = str(client_request.message[2])

            for question in questions:
                counter = 0
                sucesses = 0
                errors = 0
                if question.question == number:
                    for alternative in question.answer:
                        if alternative == answer[counter]:
                            sucesses += 1
                        else:
                            errors += 1
                        counter += 1      
                    server.sendto(f'Questão: {number}; Acertos: {sucesses}; Erros:{errors}'.encode('utf-8'), address)

def count_client_requests(address):
    counter = 0
    for client_request in requests: 
        if client_request.address == address:
            counter += 1 
    return counter

def receive():
    while True:
        # procura no array se tem 4 itens deste endereço
        client_message, address = server.recvfrom(1024)
        print(f"Requisição recebida de: {str(address)}")
        message = client_message.decode().split(";")
        requests.append(ClientRequest(address, message))

        if count_client_requests(address) == len(questions):
            handle(address)
            
receive()      


'''
while True:        
    try:
        resp = correction(number, alternatives, answer)
        num_quest = resp[0]
        sucesses = resp[1]
        errors = resp[2]
                    
        server.sendto(f'Questão: {num_quest}; Acertos: {sucesses}; Erros:{errors}'.encode('utf-8'), address)
    except:
        print(f'Erro no request recebido de: {address}.')
        server.sendto("Erro ao realizar requisição.".encode('utf-8'), address)
    except KeyboardInterrupt:
        server.sendto("Serviço finalizado.............".encode('utf-8'), address)'''