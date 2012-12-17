import sys
import os
import Image
import numpy
import scipy

if (len(sys.argv) < 3):
  print "usage: python create-image.py <path to bin files> <output image file type>"
  sys.exit(0)

path = sys.argv[1]
img_output_type = sys.argv[2]

files = os.listdir(path)

for f_name in files:
  pieces = f_name.split(".")
  if (len(pieces) > 1 and pieces[1] == "bin"):
    img_data_raw = numpy.fromfile(path+f_name, dtype=numpy.uint8).reshape(32,32,3, order="F").copy()
    img = scipy.misc.toimage(img_data_raw)
    img.save(path+pieces[0]+"."+img_output_type)

