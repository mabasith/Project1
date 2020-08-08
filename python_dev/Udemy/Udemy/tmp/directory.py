import os
import time
import tempfile
curDir = os.getcwd()
print (curDir)
os.mkdir("test")
time.sleep(10)
os.rename("test","test1")
os.rmdir('test1')
fp = tempfile.TemporaryFile()
fp.write(b'Hello World')
fp.seek(0)
fp.read()
b'Hello World'
fp.close()
#create a temporary file using a context maneger
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world')
    fb.seek(0)
    fb.read()
b'Hello World'
#create a temporary directory using the context manager

with tempfile.TemporaryFile() as tmpdirname:
    print('create temporary directory', tmpdirname)
