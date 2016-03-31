#!/usr/bin/env python

from __future__ import print_function

def neverhappen():
  if True == False:
    return "This should never happen"

if __name__ == "__main__":
  print(neverhappen())
