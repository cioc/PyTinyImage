scilab_tiny_images
==================

Was going to be Scilab version of Matlab Files http://horatio.cs.nyu.edu/mit/tiny/data/index.html

Instead created a python version


USAGE
=====

+ First use read_tiny_metadata.py to extract the indicies of files that match your keyword.  

Usage: python read_tiny_metadata.py <keyword> <max images>

e.g. python read_tiny_metadata.py cat 2000

+ Next, get the representations of these images using loadTinyImages.py:

Usage: python loadTinyImages.py <output file from read_tiny_metadata>

e.g. python loadTinyImages.py output.indices

+ Finally, use create-image.py to turn the binary files into images

Usage: python create-image.py <path to bin files> <output image type>

e.g. python create-image.py output/ png
