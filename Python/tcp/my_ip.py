import socket

class myIp:
    def __init__(self):
        self.ip = ''
        # solution found at stackoverflow
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            self.ip = s.getsockname()[0]
        except:
            self.ip = '127.0.0.1'
        finally:
            s.close()
    
    def getMyIp(self):
        return self.ip