import http.client
from http.client import HTTPSConnection
conn = htt.client.HTTPSConnection('www.google.com')
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status,r1.reason)