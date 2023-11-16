import socket 
class IPDemo: 
    def main(self): 
        host = ""
        choice = int(input("1.Enter Host Name \n2.Enter IP address \nChoice=")) 
        if choice == 1: 
            host = input("\n Enter host name: ") 
            try:
                address = socket.gethostbyname(host) 
                print("IP address: " + address) 
            
            except socket.gaierror: 
                print("Could not find " + host)
        else: 
            address = input("\n Enter IP address: ") 

            try: 
                host =  socket.gethostbyaddr(address)[0] 
                print("Host name and IP address: ", host,address) 
            except socket.gaierror: 
                print("Could not find " + host) 
IPDemo().main()
