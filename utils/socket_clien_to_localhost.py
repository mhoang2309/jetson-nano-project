import socket
import ast
import time
import sys
from flask import Flask, render_template, Response, request
from flask_cors import CORS
import random
from threading import Thread
msgFromClient ="" 
localIP     = socket.gethostname() 
localPort   = 20001
bufferSize          = 1024
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = (localIP, localPort)
list_ = []
app = Flask(__name__)
CORS(app)

class file_video:
    def __init__(self, file1):
        self.file1 = file1
class temps:
    def __init__(self, temps):
        self.temps = temps
file1 = file_video
temps1 = temps
def add_list(json):
    list_.append(json)

def receive_json():
    time_start = time.time()
    while temps1.temps == 1:
    # Create a UDP socket at client side

        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Send to server using created UDP socket

        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "{}".format(msgFromServer[0])
        a = msg.lstrip("b")
        a = a.lstrip('"')
        a = a.rstrip('"')
        res = ast.literal_eval(a)
        add_list(res)
        if time.time() - time_start >=20:
            break
        #print(res)
        #print(res)
        #jsonObj = json.loads(str(res))
        #print(jsonObj)
        # person = 0
        # for i in res:
        #     if i == "person":
        #         person = person + 1
        # print(person)
    # man = list_[0]
    # print(man["man"])
    # print(len(list_))
    return list_

def obj_max(list):
    man = 0
    girl = 0
    elder= 0
    children = 0
    obj = []
    for i in list:
       man = man + i["man"] 
       girl = girl + i["girl"]
       elder = elder + i["elder"]
       children = children + i["children"]
    obj.append(man)
    obj.append(girl)
    obj.append(elder)
    obj.append(children)
    if max(obj) == 0:
        return 0
    else:
        for i in range(len(obj)):
            if max(obj) == obj[i]:
                return i + 1

def return_video(max_obj):
    if max_obj == 0:
        return random.randint(1,6)
    if max_obj == 1:
        return 1
    if max_obj == 2:
        return 2
    if max_obj == 3:
        return 3
    if max_obj == 4:
        return 4

@app.route('/videos', methods=['GET'])
def test():
    print("....")
    print(file1.file1)
    return str(file1.file1) +'.mp4'

@app.route('/videos', methods=['POST'])
def getvideo():
    #print("okela")
    temps_ = request.json
    temps1.temps = int(temps_['temp'])
    
    # print(temps1.temps['temp'])
    # value = request.form['projectFilePath']
    # file_name = random.randint(1, 6)
    # print(value)
    # print('==================response=============')
    # print(file_name)
    return temps_

def run_server():
    app.run(host='0.0.0.0', threaded=True)

def main_host():
    temps1.temps = 1
    class_id = obj_max(receive_json())
    file1.file1 = return_video(class_id)
    list_.clear()
    print(file1.file1)
    Thread(target=run_server, args=()).start()
    while True:
        if temps1.temps == 1:
            class_id = obj_max(receive_json())
            file1.file1 = return_video(class_id)
            list_.clear()
            print("classid")
            print(class_id)
            print("video")
            print(file1.file1)

       
        
