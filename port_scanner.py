import sys
import socket

objective = socket.gethostbyname(input("Insert IP: "))

print("Scanning objective: " + objective)

try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        final = s.connect_ex((objective, port))
        if final == 0:
            print("Port {} is open.". format(port))
            s.close()
except:
    print("\n Leaving...")
    sys.exit(0)
