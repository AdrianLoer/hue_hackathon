from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
#from client import image_decoder

class SimpleEcho(WebSocket):

    def handleMessage(self):
        pass

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

#server = SimpleWebSocketServer('', 80, SimpleEcho)
#server.serveforever()

def decode(bitArray):
    s = ""
    counter = 0
    bitBuffer = ""
    while counter < len(bitArray):
        bitBuffer = "".join([str(x) for x in bitArray[counter:counter+7]])
        counter+=7
        s += chr(int(bitBuffer,2))
        bitBuffer = ""
    return s

print(decode([1,0,0,1,0,0,0,1,0,0,1,0,0,0]))