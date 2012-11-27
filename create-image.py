import Image
import numpy
import scipy

filename = "output/1.bin"

datalinear = numpy.fromfile(filename, dtype=numpy.uint8).reshape(32,32,3, order="F").copy()
img = scipy.misc.toimage(datalinear)
img.save("output/1.bmp")

