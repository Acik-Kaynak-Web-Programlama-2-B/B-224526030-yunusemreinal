from socket import *
from threading import *
 
clients = []
names = []
 
def clientThread(client):
    bayrak = True
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if bayrak:
                names.append(message)
                print(message, 'bağlandı')
                bayrak = False
            for c in clients:
                if c != client:
                    index = clients.index(client)
                    name = names[index]
                    c.send((name + ':' + message).encode('utf8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            name=names[index]
            names.remove(name)
            print(name + ' çıktı')
            break
 

def file_transfer_thread(client):
    try:
        dosya_adı = client.recv(1024).decode('utf8')
        print(f"Alınacak dosya adı: {dosya_adı}")
        with open(dosya_adı, 'wb') as file:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"{dosya_adı} dosyası başarıyla alındı.")
    except:
        print("Dosya transferi sırasında bir hata oluştu.") 
        
server = socket(AF_INET, SOCK_STREAM)
 
ip = '10.100.5.145'
port = 6666
server.bind((ip, port))
server.listen()
print('Server dinlemede...')
 
 
while True:
    client, address = server.accept()
    clients.append(client)
    print('Bağlantı yapıldı..', address[0] + ':' + str(address[1]))
    thread = Thread(target=clientThread, args=(client, ))
    thread.start()
    
    