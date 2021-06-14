import json
import socket
import select

localIP     = socket.gethostname() 
localPort   = 20001
bufferSize  = 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


def socket_net(label):
    msgFromServer = label
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket.setblocking(0)
    ready = select.select([UDPServerSocket],[],[],0.001)
    if ready[0]:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        #clientMsg = "Message from Client:{}".format(message)
        #clientIP  = "Client IP Address:{}".format(address)
        #print(clientMsg)
        #print(clientIP)
        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)

def count_cls(cls):
  return [[x,cls.count(x)] for x in set(cls)]

def convert_json(cls_json):
  m ='{"person":0,"man":0,"girl":0,"elder":0,"children":0}'
  jsonObj = json.loads(m)
  person = 0
  man = 0
  girl = 0
  elder = 0
  children = 0
  for i in cls_json:
    if i[0] == "person":
      person = i[1]
    elif  i[0] == "man":
      man = i[1]
    elif  i[0] == "girl":
      girl = i[1]
    elif  i[0] == "elder":
      elder = i[1]
    else:
      children = i[1]
  jsonObj['person'] = person
  jsonObj['man'] = man
  jsonObj['girl'] = girl
  jsonObj['elder'] = elder
  jsonObj['children'] = children
  return jsonObj