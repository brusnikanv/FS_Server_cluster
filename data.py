class Camera:
    def __init__(self, name, rtsp):
        self.name = 'Camera_name'
        self.rtsp = 'rtsp://0.0.0.0/live'

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr({'name': self.name, 'ipaddr': self.ipaddr, 'assigned': self.assigned})


class Server:
    def __init__(self, name, ipaddr, status, load):
        self.name = name
        self.ipaddr = ipaddr
        self.status = status
        self.load = load
        self.cameras = dict()

    #    def add(self, camera):
    #        self.cameras[]

    def __repr__(self):
        return repr({'name': self.name, 'ipaddr': self.ipaddr, 'status': self.status, 'status': self.load})


def test_get_servers():
    servers = list()
    servers.append(Server(name='Test', ipaddr='1.2.3.4', status='Offline', load=40))
    servers.append(Server(name='Test2', ipaddr='2.2.3.4', status='Idle', load=10))
    servers.append(Server(name='Test3', ipaddr='3.2.3.4', status='Idle', load=60))
    servers.append(Server(name='Test4', ipaddr='0.0.0.0', status='Active', load=33))
    servers.append(Server(name='Test5', ipaddr='5.5.5.5', status='Offline', load=10))
    servers.append(Server(name='Test6', ipaddr='1.2.1.4', status='Active', load=15))

    return servers


def test_get_streams():
    return
