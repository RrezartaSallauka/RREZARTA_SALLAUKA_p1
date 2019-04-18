from socket import *
import sys
serverName='localhost'
serverPort=12000
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    
    s.connect((serverName, serverPort))

    kerkesa = input("Shkruani kerkesen tuaj: ")
    s.sendall(str.encode(kerkesa))
    if  kerkesa=='1' and kerkesa is not None :
        data=s.recv(128)
        print( data.decode())
        print("\n")
        break

    elif kerkesa=="2" and kerkesa is not None:
        data=s.recv(128)
        print('Porti:',data.decode())
        print("\n")
        break

    elif kerkesa=="3" and kerkesa is not None:
        var=input("Shkruaj nje tekst :")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print('Numrim i bashketingelloreve ne fjali:',data.decode())
        print("\n")
        break

    elif kerkesa=="4" and kerkesa is not None:
        var=input("Shkruaj tekst :")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print('Rezultati nga serveri:',data.decode())
        print("\n")
        break

    elif kerkesa=="5" and kerkesa is not None:
        data=s.recv(128)
        print(data.decode())
        print("\n") 
        break
    elif kerkesa=="6" and kerkesa is not None:
        tm=s.recv(128)
        print(tm.decode('ascii'))
        print("\n")
        break

    elif kerkesa=="7" and kerkesa is not None:
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        break

    elif kerkesa=="8" and kerkesa is not None:
        var=input("Jep nje numer:")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print(data.decode())
        print("\n")
        break

    elif kerkesa=="9" and kerkesa is not None:
        var=input("Jepni numrin :")
        var=str(var)
        s.sendall(str.encode(var))
        var1=input('Zgjidhni njeren nga konvertimet: C-to-K , C-to-F , K-to-F , K-to-C , F-to-C , F-to-K , pound-to-kg , kg-to-pound: ')
        s.sendall(str.encode(var1))
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        break

   
        
    else:
        print("Kerkesa nuk mund te pranohet nga serveri!!!")
        print("\n")
        break

