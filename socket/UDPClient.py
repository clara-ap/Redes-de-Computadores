from socket import *

'''
Criação de uma aplicação cliente-servidor simples para demonstrar 
a programação de socket para UDP.
Aplicação: um cliente lê uma linha de caracteres do teclado e a 
envia para o servidor, que recebe os dados e converte os caracteres 
para maiusculas.
'''

serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) 
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

'''
serverName -> endereço IP ou hostname do servidor. se o hostname for 
utilizado, uma pessquisa DNS será automaticamente relizada.

serverPort -> número de porta

clientSocket = socket(AF_INET, SOCK_DGRAM) -> cria o socket do cliente, 
denominado clientSocket
o primeiro parâmetro indica a família do endereço. 
AF_INET -> rede subjacente usa IPv4
segundo parâmetro indica que o socket é do tipo SOCK_DGRAM -> socket UDP

message -> cria a mensagem que será enviada

clientSocket.sendto(message.encode(),(serverName, serverPort)) -> enviando
a mensagem ao hospedeiro de destino
método encode -> conversão da mensagem para bytes
método sendto -> acrescenta o endereço de destino à mensagem e envia o 
pacote resulatnte pelo socket do processo, clientSocket

modifiedMessage, serverAdress = clientSocket.recvfrom(2048) -> recepção
dos dados do servidor após envio da mensagem. os dados serão armazenados
em modifiedMessage e a variável serverAdress contém os dadso referentes 
ao endereco do servidor.
método recvfrom -> toma o tamanho do buffer como entrada

print(modifiedMessage.decode())
método decode -> converte os bytes para string
'''