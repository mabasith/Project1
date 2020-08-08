""" import urllib.request
from urllib.request import urlopen
f = urllib.request.urlopen("http://www.python.org")
print(f.read()) """
import http.client
from http.client import HTTPSConnection
from http import cookies
import urllib.request
import urllib.parse

conn = htt.client.HTTPSConnection('www.google.com')
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status,r1.reason)
C = cookies.SimpleCookie()
C["fig"] = "newton"
c["sugar"] = "cone"
url = "http://www.claydesk.com"
value = {'s':'basic','submit':'search'}
data = urllib.parse.urlencode(value)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)