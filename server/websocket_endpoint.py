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
    bitBuffer = ""
    for i in range(len(bitArray), 0, -7):
        bitBuffer = bitArray[i-7:i]
        x = "".join([str(x) for x in bitBuffer])
        try:
            s = chr(int(x, 2)) + s
        except:
            pass
    return s

print(decode([0,1,0,0,1,0,0,0,1,0,0,1,0,0,0]))