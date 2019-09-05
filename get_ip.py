

import socket
def get_ip():
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip.connect(('10.255.255.255', 1))
        IP = ip.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        ip.close()
    return IP
print(get_ip())
