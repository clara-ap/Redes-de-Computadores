from socket import *

'''
Criação de uma aplicação cliente-servidor simples para demonstrar 
a programação de socket para UDP.
Aplicação: um cliente lê uma linha de caracteres do teclado e a 
envia para o servidor, que recebe os dados e converte os caracteres 
para maiusculas.
'''

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAdress)


'''
serverSocket.bind(('', serverPort)) -> designa o número de porta 
12000 ao socket do servidor. Dessa forma, quando alguém enviar um 
pacote à porta 12000 no endereço IP do servidor, ele será direcionado 
a este socket

o laço while permite que UDPServer receba e processe pacotes dos 
clientes indefinidamente
message, clientAdress = serverSocket.recvfrom(2048) -> uma vez que os 
dados chegam no socket do servidor, eles são colocados na variável 
message e o endereço de origem, em clientAdress

modifiedMessage = message.decode().upper() -> a mensagem enviada pelo 
ciente é decodificada e passada para letras maiúsculas 

serverSocket.sendto(modifiedMessage.encode(), clientAdress) -> codifica
a mensagem modificada e anexa o endereço do cliente a ela, enviando o 
pacote resultante à rede
'''