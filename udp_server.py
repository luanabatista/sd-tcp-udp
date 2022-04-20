# Servidor: fica em aguardo de requisição de algum cliente. 
# Quando recebe uma requisição devolve uma mensagem de correção e encerra a conexão. 
import socket

questions = []
class Question:
    def __init__(self, question, alternatives, answer):
        self.question = question
        self.alternatives = alternatives
        self.answer = answer

question1 = Question(1, 4, 'VVVF')
questions.append(question1)
question2 = Question(2, 5, 'VFVFV')
questions.append(question2)
question3 = Question(3, 3, 'FFV')
questions.append(question3)
question4 = Question(4, 4, 'VFVV')
questions.append(question4)

#se existe uma questao com esse numero
#para cada questao, se existe uma de mesmo numero, entao para cada alternativa verificar se esta igual
def correction(number, alternatives, answer):
    counter = 0
    sucesses = 0
    errors = 0
    for question in questions:
        if question.question == number:
            for alternative in question.answer:
                if alternative == answer[counter]:
                    sucesses += 1
                else:
                    errors += 1
                counter += 1
    return [number, sucesses, errors]

# Cria um Socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))
print("Aguardando requisição...")

while True: 
    try:
        message_bytes, address = server.recvfrom(1024)
        message_str = message_bytes.decode()

        print(f'Request recebido de: {address}. Requisição: ({message_str})')

        message_array = message_str.split(";")
        number = int(message_array[0])
        alternatives = int(message_array[1])
        answer = str(message_array[2])

        
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
        server.sendto("Serviço finalizado.............".encode('utf-8'), address)