import socketserver
import socket
import time
import logging
import sipfullproxy
from sipfullproxy import UDPHandler

HOST, PORT = '0.0.0.0', 5060

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                    datefmt='%H:%M:%S')
logging.info("-------------------------NEW SESSION-------------------------")
logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
hostname = socket.gethostname()
logging.info(hostname)
ipaddress = socket.gethostbyname(hostname)
logging.info(ipaddress)
logging.info("-----------------------SESSION PROGRESS-----------------------")
print("Proxy server started at <%s:%s>" % (ipaddress, PORT))
sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
server = socketserver.UDPServer((HOST, PORT), UDPHandler)
server.serve_forever()
