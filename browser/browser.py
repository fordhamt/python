"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()
from socket import *

class HTTPConnection:
    def __init__(self, hostname, port = 80):
        self.hostname = hostname
        self.port = port
        self.version = "HTTP/1.0\n\n"
        self.s = socket()
        self.connect()

    def connect(self):
        self.s.connect(("Host:" + self.hostname, self.port))

    def request(self, method, url, headers = None):
        req = method + " " + url + " " + self.version
        self.s.send(req)

    def getresponse(self):
        return HTTPResponse(self.s)

    def close(self):
        self.s.close()

class HTTPResponse:
    def __init__(self, sock):
        self.s = sock

	# default vals
        self.data = None
        self.version = 1.1
        self.status = 200
        self.reason = "OK"
	self.headers = []
        self.body = []
        self.name = None
	self.isBody = False
	self.start = 0
        self.end = 0

	# grab data 
        self.f = self.s.makefile()
	self.f2 = self.s.makefile()
        # read status line and split line into the 3 values
        self.statusLine = self.f.readline().split()

        # set version
        if "1.1" in self.statusLine[0]:
            self.version = 1.1
        else:
            self.version = 1.0

        # set status
        self.status = self.statusLine[1]

        # set reason. if reason is more than one word, get all words
        if len(self.statusLine) > 3:
            self.statusLine.pop(0)
            self.statusLine.pop(0)
            self.reason = ' '.join(self.statusLine)
        else:
            self.reason = self.statusLine[2]

        for line in self.f.readlines():
            if "<html>" in line:
                self.isBody = True
            if "<!DOCTYPE html>" in line:
                self.isBody = True
            if not self.body:
                self.headers.append(line)
            if self.isBody:
                self.body.append(line)

        self.bodyText = ' '.join(self.body)

    def getheader(self, name = None):
        for line in self.headers:
            if name in line:
                return line
        return None

    def getheaders(self):
        return self.headers

    def version(self):
        return self.version

    def status(self):
        return self.status

    def reason(self):
        return self.reason

    def read(self, amt = 0):
        if amt == 0:
            return self.bodyText
        if self.end is not 0:
            self.start = self.end

        self.end += amt

        if len(self.bodyText) > self.end:
            retVal = self.bodyText[self.start:self.end]
        else:
            return self.bodyText
        return retVal

conn = HTTPConnection("www.cs.fsu.edu")
conn.request("GET", "/~carnahan/cis4930/")
resp = conn.getresponse()
print("Version: ", resp.version)
print("Status: ", resp.status)
print("Reason: ", resp.reason)
print("Headers: ", resp.getheaders())
print("Value of Date header: ", resp.getheader("Date"))
print("First 10 bytes of body: ", resp.read(10))
