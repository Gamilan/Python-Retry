#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys
import time

def main():
    visszateresi_ertek = 1
    if len(sys.argv) == 1:
        print "Hasznalat: ./futtato.py ./futtatando program [argumentumok]"
    else:
        while visszateresi_ertek:
            meghivott = subprocess.Popen(sys.argv[1:])
            meghivott.wait()
            visszateresi_ertek = meghivott.returncode
            if visszateresi_ertek:
                time.sleep(1)
  
if __name__ == "__main__":
    main()
