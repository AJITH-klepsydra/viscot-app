from urllib.request import urlopen
import time

import socket

def internet(host="8.8.8.8", port=53, timeout=3):

  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return 1
  except socket.error as ex:
    print(ex)
    return 0
k=int(internet())
url = 'https://api.covid19api.com/'
