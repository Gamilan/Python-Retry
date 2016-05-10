#!/usr/bin/env python3
# encoding: utf-8

import subprocess
import sys
import time

WAIT = 1

def main():
    if len(sys.argv) == 1:
        print("Usage: {0} command [arguments]".format(sys.argv[0]))
    else:
        while True:
            command = subprocess.Popen(sys.argv[1:])
            command.wait()
            if command.returncode != 0:
                time.sleep(WAIT)
            else:
                break
  
if __name__ == "__main__":
    main()
