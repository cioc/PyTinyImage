import sys
import os

if (len(sys.argv) < 2):
  print "usage: python loadGroundTruth.py <keyword>"
  sys.exit(0)

keyword = sys.argv[1]

f = open("annotations.txt", "r")

output = []
for l in f.readlines():
  pieces = l.split(" ")
  if (len(pieces) > 5):
    if pieces[1] == keyword and int(pieces[2]) == 1:
      output.append(int(pieces[5].strip()))
      
print output   


