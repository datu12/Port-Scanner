import socket
import sys
from datetime import datetime



#ip portrange (ASK FOR INPUT)

remoteServer = input(" + Enter remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("\n")
print(" [*] Please wait scanning host")

t1 = datetime.now()

# port will be iterated in range 1 - 65000

def main():
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((remoteServerIP,port))
        if result == 0:
            print(" [*] Port {}:  Open".format(port))        
        s.close()

if __name__ == "__main__":
    main()

  
t2 = datetime.now()
total = t2 - t1
print(" [*] Scanning completed in: {}".format(total))
