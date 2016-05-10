#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys
import time

def main():
    returncode = 1
    if len(sys.argv) == 1:
        print "Usage: ./futtato.py command [arguments]"
    else:
        while returncode:
            command = subprocess.Popen(sys.argv[1:])
            command.wait()
            returncode = command.returncode
            if returncode:
                time.sleep(1)
  
if __name__ == "__main__":
    main()
