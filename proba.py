#!/usr/bin/env python
# encoding: utf-8

import random as r
import sys

def main():
    if r.randint(1, 5) == 3:
        print "OK"
    else:
        print "error"
        sys.exit(1)

##############################

if __name__ == "__main__":
    main()
