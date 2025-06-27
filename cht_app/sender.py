import socket  ## used to set up communication over a network
try:
    ## creating sockets
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ##dgram -- datagram -- used to transfer messages
    ##ip add -- ipv4 address -- af inet -- address family -- it less socket that we use ipv4 address
    print("socket created")
    
    ip = "192.168.43.89"
    port = 222              ## port no. size --> 0-65535
    target_add = (ip,port)
    message = input("enter the message:-->")
    encoded_message = message.encode("ascii")
    s.sendto(encoded_message,target_add) 
    print("message sent")
    s.close()
except Exception as e :
    print("",e)
    
    
    
    
    ## steps to run project 
    #1 --> you have to connect with the same network
    #2 --> take port no. same in both file
    #3 --> windows firewall off rkhna h 
    #4 --> sbsa phla receiver ki file chlge 