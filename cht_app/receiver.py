import socket 
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ##dgram -- datagram -- used to transfer messages
    ##ip add -- ipv4 address -- af inet -- address family -- it less socket that we use ipv4 address
    print("socket created")
    
    
    ## sender ke file m ip address receiver ka ayaga hmesha
    ## and receiver me receiver ka he aayga 
    
    ip = "192.168.43.89"
    port = 222
    complete_add = (ip,port)
    s.bind(complete_add)
    
    while True:
        message , senders_address = s.recvfrom(1024)
         ## limit // size 1024 bytes
         
        print("Raw Message",message)
        print("Sender Address",senders_address)
         
        decoded_msg = message.decode("ascii")
        print("Decoded Message",decoded_msg)
         
except Exception as e:
    print("An error occured",e)