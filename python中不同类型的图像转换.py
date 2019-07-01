"""
该文件中的代码来自此链接。
http://wanda.fiu.edu/boeglinw/downloads/Dust/Image%20analysis/convert.py

"""
#
# A collection of image converstion routines
#
import wx           # wx
import numpy as n   # numpy
import Image as I   # PIL

# file = 'Rotating_earth/Rotating_earth119.jpg'
# file = 'helincolia.jpg'

idata_type = 'uint8'
# fdata_type is not used so far
fdata_type = 'float'

#----------------------------------------------------------------------
# convert wx image to numpy array
#----------------------------------------------------------------------
def wx_to_numpy( original_image , color = True):
    if color == True :
        image = original_image
    else:
        image = original_image.ConvertToGreyscale()
    # get image size
    dimx = image.GetWidth()
    dimy = image.GetHeight()
    # get the raw image data
    image_data = image.GetData()
    image_data_string=n.fromstring(image_data,dtype=idata_type)
    if color == True:
        return image_data_string.reshape((dimy, dimx, 3)) # return the whole image
    else:
        return image_data_string.reshape((dimy, dimx, 3))[:,:,0] # return a smaller part
#end of wx_to_numpy
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# convert numpy array to wx image
#----------------------------------------------------------------------
def numpy_to_wx(original_image):
    # check if array contains color information
    if (len(original_image.shape) == 3) : # color image
        # it is an array with color information, get size information
        dimy, dimx, ncol = original_image.shape
        image_data = original_image.tostring()
        return wx.ImageFromData(dimx, dimy, image_data)
    elif (len(original_image.shape) == 2) : # B&W image
        dimy, dimx = original_image.shape
        wx_data = (n.dstack((original_image, original_image, original_image))).tostring()
        return wx.ImageFromData(dimx,dimy,wx_data)
    else:
        print 'numpy_to_wx: not an image array !'
        return None
# end of numpy_to_wx
#----------------------------------------------------------------------


#----------------------------------------------------------------------
# convert PIL image to numpy array
#----------------------------------------------------------------------
def numpy_to_PIL(original_image):
    return I.fromarray(original_image.astype(idata_type))
#----------------------------------------------------------------------
# convert numpy array to PIL image
#----------------------------------------------------------------------
def PIL_to_numpy(original_image, color = True):
    if color == True :
        return n.asarray(original_image).astype(idata_type)
    else:
        return n.asarray(original_image.convert('L')).astype(idata_type)
#----------------------------------------------------------------------