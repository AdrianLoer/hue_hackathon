from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from client import image_decoder

class SimpleEcho(WebSocket):

    def handleMessage(self):
        image_decoder

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 80, SimpleEcho)
server.serveforever()