import sys
import os
import gc

if (len(sys.argv) < 2):
  print "usage: python loadTinyImages.py <path_to_indices_file>"
  sys.exit(0)

indices_path = sys.argv[1]

data_file_path = "/tiny/tinyimages/tiny_images.bin"
output_path = "output/"

f = open(data_file_path, "rb")

def sliceToBin(indx):
  offset = indx * 3072
  f.seek(offset)
  data = f.read(3072) 
  o = open(output_path+str(indx)+".bin", "wb")
  o.write(data)
  o.close()

g = open(indices_path, "r")

for l in g.readlines():
  sliceToBin(int(l.strip()))

f.close()
