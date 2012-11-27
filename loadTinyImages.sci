function [img] = loadTinyImages(ndx,filename)

// Output variables initialisation (not found in input variables)
img=[];

// Number of arguments in function call
[%nargout,%nargin] = argn(0)

// Display mode
mode(0);

// Display warning for floating point exception
ieee(1);

// 
// Random access into the file of tiny images.
// 
// It goes faster if ndx is a sorted list
// 
// Input:
//    ndx = vector of indices
//    filename = full path and filename
// Output:
//    img = tiny images [32x32x3xlength(ndx)]

if %nargin==1 then
  filename = "/tiny/tinyimages/tiny_images.bin";
  outputdir = "/tiny/tinyimages/code/scilab_tiny_images/output/";
end;

// Images
sx = 32;
Nimages = max(size(ndx));
nbytesPerImage = (sx*sx)*3;
img = zeros((sx*sx)*3,Nimages);

// Pointer
pointer = mtlb_s(ndx,1)*nbytesPerImage;
offset = pointer;
offset = mtlb_i(offset,2:$,offset(2:$)-offset(1:$-1)-nbytesPerImage);

// Read data
[fid,message] = mtlb_fopen(filename,"r");
if fid==(-1) then
  error(message);
end;
mseek(0,fid)
for i = 1:Nimages
  mseek(offset(i),fid,"cur");
  // L.37: No simple equivalent, so mtlb_fread() is called.
  tmp = mtlb_fread(fid,nbytesPerImage,"uc");
  [ofid, err] = mopen(outputdir + string(i) + ".bin", "w");
  mput(tmp, "uc", ofid);
  mclose(ofid);
  img(:,i) = tmp;
end;
mclose(fid);

img = matrix(img,32,32,3,Nimages);

endfunction
