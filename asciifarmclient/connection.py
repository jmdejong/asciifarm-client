
import socket

from asciifarmclient.common.tcommunicate import send, receive
from asciifarmclient.common import messages
import json

class Connection:
    
    def __init__(self, socketType):
        if socketType == "abstract" or socketType == "unix":
            sockType = socket.AF_UNIX
        elif socketType == "inet" or socketType == "inet4":
            sockType = socket.AF_INET
        elif socketType == "inet6":
            sockType = socket.AF_INET6
        else:
            raise ValueError("Invalid socket type: %r" % (socketType,))
        self.sock = socket.socket(sockType, socket.SOCK_STREAM)
    
    def connect(self, address):
        self.sock.connect(address)
    
    def receive(self):
        databytes = receive(self.sock)
        if len(databytes) == 0:
            return None
        datastr = databytes.decode('utf-8')
        msg = json.loads(datastr)
        message = messages.message_from_json(msg)
        return message
    
    def listen(self, callback, onError):
        while True:
            try:
                message = self.receive()
            except Exception as err:
                onError(err)
            else:
                callback(message)
    
    def send(self, message):
        send(self.sock, message.to_json_bytes())
