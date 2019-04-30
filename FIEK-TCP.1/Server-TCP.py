from socket import*
import _thread
import time
from socket import gethostname;
import random
import datetime
import math

print ('                                                UNIVERSITETI I PRISHTINES                                                ')
print ('                                      Fakulteti i Inxhinierise Elektrike dhe Kompjuterike                                ')
serverName = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('                                               Serveri eshte gati te pranoj kerkese                                        ')


def CThread(serverSocket,clientAdd,kerkesa):
 
    
    def IPADRESA(): 
            connS.send(str("IP Adresa e klientit eshte:" +str(clientAdd[0])).encode('ASCII'))
   
    def NUMRIIPORTIT():
            connS.send(str(str(clientAdd[1])).encode('ASCII'))

    def BASHKETINGELLORE(teksti):
        nrBashketingellore = 0
        nrBashketingelloreve = ['Q', 'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J','K','L','Z','X','C','V','B','N','M','q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        for i in teksti:
            if i in nrBashketingelloreve:
                nrBashketingellore += 1
        connS.send(str("Numri i bashketingelloreve ne fjalen e dhene eshte:" +str(nrBashketingellore)).encode('ASCII'))
 

    def PRINTIMI():
        data=connS.recv(128)
        print(data)
        connS.send(data)
    
    def EMRIIKOMPJUTERIT():
        emri=''
        if gethostname()==None :
            emri='\Emri i klientit nuk dihet !\n'
        else:
            emri='Emri i klientit eshte:'+gethostname()

        print(emri)
        connS.send(str.encode(emri))

    def KOHA():
        koha=time.strftime('%d/%b/%Y %X')
        connS.send(str(str(koha)).encode('ASCII'))

    def LOJA():
        loja=[random.randint(1,49) for i in range(7)]
        connS.send(str(str(loja)).encode('ASCII'))

    def FIBONACCI(nr1):
         a,b = 1,1
         for i in range(int(nr1)-1):
             a,b = b,a+b
         connS.send(str("Numri FIBONACCI eshte: "+ str(a)).encode('ASCII'))

    def KONVERTIMI(temperatura,x):
        if x=="C-to-K": 
            temperatura=str(float (float(temperatura)+273.00))
            connS.send(str.encode(str(temperatura)))

       
        elif x=="C-to-F":
            temperatura= str(1.8 * float(float(temperatura)+32))
            connS.send(str.encode(str(temperatura)))  
        

        elif x=="K-to-F":
            temperatura=str(1.8 * float(float(temperatura)-273)+32)
            connS.send(str.encode(str(temperatura)))  
        
       
        elif x=="K-to-C":
            temperatura=str(float(float(temperatura)-273))
            connS.send(str.encode(str(temperatura)))  
       

        elif x=="F-to-C":
            temperatura=str(5/9*float(float(temperatura))-32)
            connS.send(str.encode(str(temperatura)))  
       
      
        elif x=="F-to-K":
            temperatura=str(5/9*float(float(temperatura)-32)+273)
            connS.send(str.encode(str(temperatura)))  
   

        elif x=="pound-to-kg":
            c=str(float(float(temperatura))/2.20462262)
            connS.send(str.encode(str(c)))  
       
        elif x=="kg-to-pound":
            c=str(float(float(temperatura))*2.20462262)
            print(c)
            connS.send(str.encode(str(c))) 
   
        else:
            print('Kerkesa juaj nuk mund te pranohet !')
            connS.send(str.encode('Kerkesa juaj nuk mund te pranohet'))

    def INCH(numrii,x):
        a=2.54
        if x=="INCH-TO-CM":
            numrii=str(float(float(numrii)*2.54))
            print(numrii)
            connS.send(str.encode(numrii))

        elif x=="CM-TO-INCH":
            numrii=str(float(float(numrii)/a))
            print(numrii)
            connS.send(str.encode(numrii))



    def PERIMETRI(r):
        rrezja = float (r)
        perimteri = math.pi*rrezja
        connS.send(str("Perimteri i rrethit eshte:" +str(perimteri)).encode('ASCII'))
    



    if kerkesa=='1':
         IPADRESA()

    elif kerkesa=='2':
        NUMRIIPORTIT()

    elif kerkesa=='3':
        data1=connS.recv(128)
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
        data2=connS.recv(128)
        data2=data2.decode()
        print(data2)
        FIBONACCI(int(data2))
           
    

    elif kerkesa=='9':
        data2=connS.recv(128)
        data2=data2.decode()
        print(data2)
        data3=connS.recv(128)
        data3=data3.decode()
        print(data3)
        KONVERTIMI(data2,data3)

    elif kerkesa=='10':
        data4=connS.recv(128)
        data4=data4.decode()
        print(data4)
        PERIMETRI(int(data4))


    elif kerkesa=='11':
        data2=connS.recv(128)
        data2=data2.decode()
        print(data2)
        data3=connS.recv(128)
        data3=data3.decode()
        print(data3)
        INCH(data2,data3)  
   
    

      
while 1: 
    connS, clientAdd = serverSocket.accept()
    kerkesa = connS.recv(128)
    kerkesa = kerkesa.decode('ASCII')
    _thread.start_new_thread(CThread,(serverSocket,clientAdd,kerkesa))
connS.close()


    
   



