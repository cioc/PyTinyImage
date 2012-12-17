#function library for tiny image dataset
import numpy
import scipy
import Image

#paths to various data files
meta_file_path = "/tiny/tinyimages/tiny_metadata.bin"
data_file_path = "/tiny/tinyimages/tiny_images.bin"
 
#open data files
meta_file = 0
data_file = 0

def openTinyImage():
 	global meta_file
	global data_file
	meta_file = open(meta_file_path, "rb")
	data_file = open(data_file_path, "rb")

def strcmp(str1, str2):
  l = min(len(str1), len(str2)) 
  for i in range(0, l):
    if (ord(str1[i]) > ord(str2[i])):
      return 1
    if (ord(str1[i]) < ord(str2[i])):
      return -1
  if (len(str1) > len(str2)):
    return 1
  if (len(str1) < len(str2)):
    return -1
  return 0

#only keyword and filename actually work right now
def getMetaData(indx):
  offset = indx * 768
  meta_file.seek(offset)
  data = meta_file.read(768)
  keyword = data[0:80].strip()
  filename = data[80:185].split(" ")[0]
  width = data[185:187]
  height = data[187:189]
  color = data[189:190]
  date = data[190:222]
  engine = data[222:232]
  thumbnail = data[232:432]
  source = data[432:760]
  page = data[760:764]
  indpage = data[764:768]
  indengine = data[768:762]
  indoverall = data[762:764]
  label = data[764:768]
  return (keyword, filename, width, height, color, date, engine, thumbnail, source, page, indpage, indengine,indoverall, label)

img_count = 79302017

def logSearch(term):
  low = 0
  high = img_count
  for i in range(0, 9):
    meta = getMetaData(int((low + high) / 2))
    cmp = strcmp(meta[0].lower(), term.lower())
    if (cmp == 0):
      return (low, high)
    if (cmp == 1):
      high = ((low + high) / 2)
    if (cmp == -1):
      low = ((low + high) / 2)
  return (low, high)

def retrieveByTerm(search_term, max_pics):
	(l, h) = logSearch(search_term)
	found = False
	found_count = 0
	o = []
	for i in range(l, h):
		meta = getMetaData(i)
		if meta[0].lower() == search_term.lower():
			found = True
			o.append(i)
			found_count += 1
			if (found_count == max_pics):
				break
		else:
			if (found):
				break  
	return o

def sliceToBin(indx):
  offset = indx * 3072
  data_file.seek(offset)
  data = data_file.read(3072) 
  return numpy.fromstring(data, dtype='uint8')

def sliceToImage(data, path):
	t = data.reshape(32,32,3, order="F").copy()
	img = scipy.misc.toimage(t)
	img.save(path)

def closeTinyImage():
	data_file.close()
	meta_file.close()	
