from socket import *
from threading import *
from tkinter import *

client = socket(AF_INET, SOCK_STREAM)

ip = '10.100.5.145'
port = 6666

client.connect((ip,port))

pencere = Tk()
pencere.title("Bağlandı : "   +ip      +" "      + str(port))

message = Text(pencere, width=50)
message.grid(row=0,column=0, 
             padx=10, pady=10)

mesaj_giris= Entry(pencere, width=50)
mesaj_giris.insert(0, "Adınız")

mesaj_giris.grid(row=1, column=0, 
                 padx=10, pady=10)
mesaj_giris.focus()
mesaj_giris.selection_range(0, END)

def mesaj_gonder():
    istemci_mesaji = mesaj_giris.get()
    message.insert(END, '\n' + 'Sen :'
                   + istemci_mesaji)
    client.send(istemci_mesaji.encode('utf8'))
    mesaj_giris.delete(0, END)
    
btn_msg_gonder = Button(pencere, text='Gönder',
                        width=15, 
                        command=mesaj_gonder)
btn_msg_gonder.grid(row=2, column=0, 
                    padx=10, pady=10)

def mesaj_gonder():
    istemci_mesaji = mesaj_giris.get()
    message.insert(END, '\n' + 'Sen :'
                   + istemci_mesaji)
    client.send(istemci_mesaji.encode('utf8'))
    mesaj_giris.delete(0, END)


def gelen_mesaj_kontrol():
    while True:
        server_msg=client.recv(1024).decode('utf8') 
        message.insert(END, '\n'+ server_msg)
 
mesaj_giris.bind('<Return>',lambda event=None: btn_msg_gonder.invoke()) 
    
recv_kontrol = Thread(target=gelen_mesaj_kontrol)
recv_kontrol.daemon = True
recv_kontrol.start()
pencere.mainloop()




