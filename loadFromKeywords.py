import sys
import os
import tinyimage

if (len(sys.argv) < 4):
  print "usage: python loadFromKeywords <keyword,keyword,keyword,...> <max> <output path>"
  sys.exit(1)


#todo - start here
keywords = sys.argv[1].split(',')
max_pics = int(sys.argv[2])
output_path = sys.argv[3]

tinyimage.openTinyImage()

for keyword in keywords:
	os.mkdir(output_path+"/"+keyword)
	indexes = tinyimage.retrieveByTerm(keyword, max_pics)
	for i in indexes:
		tinyimage.sliceToImage(tinyimage.sliceToBin(i), output_path+"/"+keyword +"/"+str(i)+".png") 			

tinyimage.closeTinyImage()


