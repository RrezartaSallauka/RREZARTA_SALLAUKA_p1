import socket
serverName='localhost'
serverPort=12000
print ('                                                UNIVERSITETI I PRISHTINES                                            ')
print ('                                      Fakulteti i Inxhinierise Elektrike dhe Kompjuterike                            ')

print('\n')
print('                                                 Zgjidhni funksionin:                                                 ')
print('\n')
print('                                                 1.IP ADDRESSA                                                       ')
print('                                                 2.NUMRI I PORTIT                                                     ')
print('                                                 3.BASHKETINGELLORET                                                  ')
print('                                                 4.PRINTIMI                                                           ')
print('                                                 5.EMRI I KOMPJUTERIT                                                 ')
print('                                                 6.KOHA                                                               ')
print('                                                 7.LOJA                                                               ')
print('                                                 8.FIBONACCI                                                          ')
print('                                                 9.KONVERTIMI                                                         ')
print('                                                 10.PERIMETRI                                                         ')
print('                                                 11.INCH                                                              ')
print('\n')

while 1:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName, serverPort))



    kerkesa = input("Shkruani numrin e kerkeses suaj: ")
    s.sendall(str.encode(kerkesa))
    if  kerkesa=='1' and kerkesa is not None :
        data=s.recv(128)
        print( data.decode())
        print("\n")
        

    elif kerkesa=="2" and kerkesa is not None:
        data=s.recv(128)
        print('Porti:',data.decode())
        print("\n")
        

    elif kerkesa=="3" and kerkesa is not None:
        var=input("Shkruaj nje tekst :")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print(data.decode())
        print("\n")
        

    elif kerkesa=="4" and kerkesa is not None:
        var=input("Shkruaj tekst :")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print('Rezultati nga serveri:',data.decode())
        print("\n")
        

    elif kerkesa=="5" and kerkesa is not None:
        data=s.recv(128)
        print(data.decode())
        print("\n") 
        
    elif kerkesa=="6" and kerkesa is not None:
        tm=s.recv(128)
        print(tm.decode('ascii'))
        print("\n")
        

    elif kerkesa=="7" and kerkesa is not None:
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        

    elif kerkesa=="8" and kerkesa is not None:
        var=input("Jep nje numer:")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print(data.decode())
        print("\n")
        

    elif kerkesa=="9" and kerkesa is not None:
        var=input("Jepni numrin :")
        var=str(var)
        s.sendall(str.encode(var))
        var1=input('Zgjidhni njeren nga konvertimet: C-to-K , C-to-F , K-to-F , K-to-C , F-to-C , F-to-K , pound-to-kg , kg-to-pound: ')
        s.sendall(str.encode(var1))
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        

    

    elif kerkesa=="10" and kerkesa is not None:
         var=input("Jepni numrin:")
         var=str(var)
         s.sendall(str.encode(var))     
         data=s.recv(128)
         print(data.decode())
         print("\n")
         




    elif kerkesa=="11" and kerkesa is not None:
        var=input("Jepni numrin:")
        var=str(var)
        s.sendall(str.encode(var))
        var1=input("Zgjedhni njeren nga opcionet INCH-TO-CM ose CM-TO-INCH:")
        s.sendall(str.encode(var1))
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        


   
        
    else:
        print("Kerkesa nuk mund te pranohet nga serveri!!!")
        print("\n")
        


