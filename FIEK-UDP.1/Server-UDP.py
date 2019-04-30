from socket import *
import time
import re
from socket import gethostname;
import random
import datetime
import math
import sys
import string
import _thread
UDP_IP="localhost"
UDP_PORT=12000
serverSocket =socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',UDP_PORT))





print ("                                                UNIVERSITETI I PRISHTINES                                             ")
print ("                                      Fakulteti i Inxhinieris Elektrike dhe Kompjuterike                              ")
print ("                                                Departamenti i Kompjuterikes                                          ")

print("\n\n\n\n")
print('                                               Serveri eshte gati te pranoj kerkese                                        ')


def CThread(serverSocket,clientAdd,kerkesa):
    clientAdd =serverSocket.recvfrom(128)
 
    
    def IPADRESA(): 
            serverSocket.sendto(str("IP Adresa e klientit eshte:" +str(clientAdd[0])).encode('ASCII'),clientAdd)
   
    def NUMRIIPORTIT():
            serverSocket.sendto(str(str(clientAdd[1])).encode('ASCII'),clientAdd)

    def BASHKETINGELLORE(teksti):
        nrBashketingellore = 0
        nrBashketingelloreve = ['Q', 'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J','K','L','Z','X','C','V','B','N','M','q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        for i in teksti:
            if i in nrBashketingelloreve:
                nrBashketingellore += 1
        serverSocket.sendto(str("Numri i bashketingelloreve ne fjalen e dhene eshte:" +str(nrBashketingellore)).encode('ASCII'),clientAdd)
 

    def PRINTIMI():
        data=serverSocket.recv(128)
        print(data)
        serverSocket.sendto(data,clientAdd)
    
    def EMRIIKOMPJUTERIT():
        emri=''
        if gethostname()==None :
            emri='\Emri i klientit nuk dihet !\n'
        else:
            emri='Emri i klientit eshte:'+gethostname()

        print(emri)
        serverSocket.sendto(str.encode(emri),clientAdd)

    def KOHA():
        koha=time.strftime('%d/%b/%Y %X')
        serverSocket.sendto(str(str(koha)).encode('ASCII'),clientAdd)

    def LOJA():
        loja=[random.randint(1,49) for i in range(7)]
        serverSocket.sendto(str(str(loja)).encode('ASCII'),clientAdd)

    def FIBONACCI(nr1):
         a,b = 1,1
         for i in range(int(nr1)-1):
             a,b = b,a+b
         serverSocket.sendto(str("Numri FIBONACCI eshte: "+ str(a)).encode('ASCII'),clientAdd)

    def KONVERTIMI(temperatura,x):
        if x=="C-to-K": 
            temperatura=str(float (float(temperatura)+273.00))
            serverSocket.sendto(str.encode(str(temperatura)),clientAdd)

       
        elif x=="C-to-F":
            temperatura= str(1.8 * float(float(temperatura)+32))
            serverSocket.sendto(str.encode(str(temperatura)),clientAdd)  
        

        elif x=="K-to-F":
            temperatura=str(1.8 * float(float(temperatura)-273)+32)
            serverSocket.sendto(str.encode(str(temperatura)),clientAdd)  
        
       
        elif x=="K-to-C":
            temperatura=str(float(float(temperatura)-273))
            serverSocket.sendto(str.encode(str(temperatura)),clientAdd)  
       

        elif x=="F-to-C":
            temperatura=str(5/9*float(float(temperatura))-32)
            serverSocket.sendto(str.encode(str(temperatura)),clientAdd)  
       
      
        elif x=="F-to-K":
            temperatura=str(5/9*float(float(temperatura)-32)+273)
            serverSocket.sendto(str.encode(str(temperatura)),clientAdd)  
   

        elif x=="pound-to-kg":
            c=str(float(float(temperatura))/2.20462262)
            serverSocket.sendto(str.encode(str(c)),clientAdd)  
       
        elif x=="kg-to-pound":
            c=str(float(float(temperatura))*2.20462262)
            print(c)
            serverSocket.sendto(str.encode(str(c)),clientAdd) 
   
        else:
            print('Kerkesa juaj nuk mund te pranohet !')
            serverSocket.sendto(str.encode('Kerkesa juaj nuk mund te pranohet'),clientAdd)

    def INCH(numrii,x):
        a=2.54
        if x=="INCH-TO-CM":
            numrii=str(float(float(numrii)*2.54))
            print(numrii)
            serverSocket.sendto(str.encode(numrii),clientAdd)

        elif x=="CM-TO-INCH":
            numrii=str(float(float(numrii)/a))
            print(numrii)
            serverSocket.sendto(str.encode(numrii),clientAdd)



    def PERIMETRI(r):
        rrezja = float (r)
        perimteri = math.pi*rrezja
        serverSocket.sendto(str("Perimteri i rrethit eshte:" +str(perimteri)).encode('ASCII'),clientAdd)
    



    if kerkesa=='1':
         IPADRESA()

    elif kerkesa=='2':
        NUMRIIPORTIT()

    elif kerkesa=='3':
        data1=serverSocket.recv(128)
        data1=data1.decode()
        print(data1)
        BASHKETINGELLORE(data1)
    elif kerkesa=='4':
        PRINTIMI()

    elif kerkesa=='5':
       EMRIIKOMPJUTERIT()

    elif kerkesa=='6':
        KOHA()

    elif kerkesa=='7':
        LOJA()
   
    elif kerkesa=='8':
        data2=serverSocket.recv(128)
        data2=data2.decode()
        print(data2)
        FIBONACCI(int(data2))
           
    

    elif kerkesa=='9':
        data2=serverSocket.recv(128)
        data2=data2.decode()
        print(data2)
        data3=serverSocket.recv(128)
        data3=data3.decode()
        print(data3)
        KONVERTIMI(data2,data3)

    elif kerkesa=='10':
        data4=serverSocket.recv(128)
        data4=data4.decode()
        print(data4)
        PERIMETRI(int(data4))


    elif kerkesa=='11':
        data2=serverSocket.recv(128)
        data2=data2.decode()
        print(data2)
        data3=serverSocket.recv(128)
        data3=data3.decode()
        print(data3)
        INCH(data2,data3)  
   
    

      
while 1: 
    kerkesa,clientAdd =serverSocket.recvfrom(128)
    print("Kerkesa:"+kerkesa.decode("ASCII"))
    _thread.start_new_thread(CThread(serverSocket,clientAdd,kerkesa))











































    
   



