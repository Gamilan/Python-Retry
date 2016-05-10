#!/usr/bin/env python3
# encoding: utf-8

import subprocess
import sys
import time

def main():
    if len(sys.argv) == 1:
        print("Usage: sys.argv[0] command [arguments]")
    else:
        while True:
            command = subprocess.Popen(sys.argv[1:])
            command.wait()
            returncode = command.returncode
            if returncode:
                time.sleep(1)
            else:
                break
  
if __name__ == "__main__":
    main()
