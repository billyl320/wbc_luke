import scipy.misc as sm
import mgcreate as mgc
import scipy.ndimage as nd
import scipy.signal as ss
import numpy as np
import skimage as sk
from sklearn import cluster
from skimage import filters
from skimage import feature
from skimage.color import label2rgb
from skimage.feature import corner_harris, corner_peaks
from skimage import exposure
import os
import math
import colorsys

#convert image to square centered at center of image
#assuming input has the shape as black
def convert(fname, bname):
    print(fname)
    #adata = bin_edges(fname=fname, bname=bname)
    adata = simp(fname=fname, bname=bname)
    #plopping into square centered at center of image with max of original image
    d = max(adata.shape)*2
    pic = mgc.Plop(adata, (d, d), 0)
    #swapping black and white
    new = pic
    #new = 1-new
    # find the center of mass
    v = nd.center_of_mass(new)
    v = (int(v[0]), int(v[1]))
    #finding cetner of new image
    n = (d/2, d/2)
    #shift in horizontal
    hori = v[1]-n[1]
    #shift in vertical
    vert = v[0]-n[0]
    #shift the image
    ultima = nd.shift(new, (-vert, -hori), cval=0)
    return ultima

#finding minimum encompassing circle - needs to be binary (1 and 0)
def enc_circ(pic):
    ultima = pic + 0
    v,h = ultima.shape
    z = np.ones((v,h))+0
    z[v//2,h//2] = 0
    dist = nd.distance_transform_edt(z)
    vals = dist*ultima
    r = vals.max()
    r = math.ceil(r)
    ultima = ultima[(v//2 - r) : r + v//2, h//2 -r : r + h//2]
    return ultima

#from page 266 of Kinser (2018)
#gives some shape metrics
#this version only provides eccentricity
def Metrics(orig):
    v, h = orig.nonzero()
    mat = np.zeros((2, len(v)))
    mat[0] = v
    mat[1] = h
    evls, evcs = np.linalg.eig(np.cov(mat))
    eccen = evls[0]/evls[1]
    if eccen < 1: eccen = 1/eccen
    return eccen, evls[0], evls[1]

def Shapes(pic):
    #clean image
    #pic = nd.gaussian_filter(pic, sigma=1.5)
    #pic = (pic > 0.99) +0.0
    #pic = (nd.binary_erosion(pic , iterations=20))+0.0
    #pic = (nd.binary_dilation(pic , iterations=20))+0.0
    #setup
    shapes = np.zeros((1,14))
    #obtain circularity
    circ = ( sum(sum((nd.binary_dilation(pic , iterations=1) - pic ))) **2) /(4*np.pi*sum(sum(pic)))
    shapes[0][0] = circ
    #provides eccentricity, eigen1 and eigen2
    eccen, e1, e2 = Metrics(pic)
    shapes[0][1] = eccen
    shapes[0][2] = e1
    shapes[0][3] = e2
    #number of corners
    corners = corner_harris(pic, k=0.1, sigma=2)
    shapes[0][4] = corner_peaks(corners, min_distance=1).shape[0]
    #white and black pixel counts for min bounding box
    slice_x, slice_y = nd.find_objects(pic==1)[0]
    roi = pic[slice_x, slice_y]
    shapes[0][5] = np.unique(roi, return_counts=True)[1][1]
    shapes[0][6] = np.unique(roi, return_counts=True)[1][0]
    #calculting moments from data
    m = sk.measure.moments(pic)
    #centroid
    centroid = (m[0, 1] / m[0, 0], m[1, 0] / m[0, 0])
    #central moments
    mu = sk.measure.moments_central(pic, centroid)
    #normalizing moments
    nu = sk.measure.moments_normalized(mu)
    #calculting hu moments
    shapes[0][7:14] = sk.measure.moments_hu(nu)
    return shapes

#extract color metrics; requires shape to be extracted first
def Colors(pic, mask):
    #setup
    colors = np.zeros((1,14))
    #convert color image to 3 extracted channels of r, g, b
    r = pic[:,:,0]
    g = pic[:,:,1]
    b = pic[:,:,2]
    #get location of flatten mask values
    vals = np.where(mask.flatten()==1.0)
    #extarct mean color for r, g, b
    colors[0][0] = r.flatten()[vals].mean()
    colors[0][1] = r.flatten()[vals].std()
    colors[0][2] = g.flatten()[vals].mean()
    colors[0][3] = g.flatten()[vals].std()
    colors[0][4] = b.flatten()[vals].mean()
    colors[0][5] = b.flatten()[vals].std()
    #now collecting cmyk
    pic_new = rgb2cmyk(pic)
    c = pic_new[:,:,0]
    m = pic_new[:,:,1]
    y = pic_new[:,:,2]
    k = pic_new[:,:,3]
    colors[0][6] = c.flatten()[vals].mean()
    colors[0][7] = c.flatten()[vals].std()
    colors[0][8] = m.flatten()[vals].mean()
    colors[0][9] = m.flatten()[vals].std()
    colors[0][10] = y.flatten()[vals].mean()
    colors[0][11] = y.flatten()[vals].std()
    colors[0][12] = k.flatten()[vals].mean()
    colors[0][13] = k.flatten()[vals].std()
    return colors

#performs needed setup for other functions
#also provides binary edges info
#must use first
def bin_edges (fname, bname):#, thresh=2 ):
    #read in image as color
    adata = sm.imread(fname, flatten=True)
    #find edges
    gdata= np.abs(np.gradient( adata ))
    val = 6.00
    ddata = ((gdata[0]>val) + (gdata[1]>val) +0.0)+0.0
    ############
    #fill holes
    ############
    shape = nd.binary_fill_holes(ddata+0.0) + 0.0
    #################################
    #get shape closest to the center
    #################################
    pic = shape +0.0
    b, n = nd.label((pic>0.0)+0.0)
    #finding center of image
    v, h = pic.shape
    #creating distance reference image
    z = np.ones((v,h))+0
    z[v//2,h//2] = 0
    dist = nd.distance_transform_edt(z)
    #getting shapes times distance from center of image
    vals = dist*pic
    #finding biggest shapes (except 0s)
    simp = np.hstack(b)
    locs= np.nonzero( simp )
    counts=np.bincount(simp [locs] )
    vals=counts.argsort()[-3:][::-1]
    clist = list(map(lambda x: b==x, (0,vals[0]) ))
    shape = (clist[1]+0)
    sm.imsave(bname+fname[53:-3]+'png', shape+0.0)
    shape = (clist[1]+0)
    ############
    #fill holes
    ############
    #shape = nd.binary_fill_holes(shape+0.0) + 0.0
    #shape = (shape>0) + 0.0
    sm.imsave(bname+fname[53:-3]+'png', shape+0.0)
    return shape

#does this for each pixel
def rgb_to_cmyk(r, g, b):
    RGB_SCALE = 255
    CMYK_SCALE = 255
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE
    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE
    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    # rescale to the range [0,CMYK_SCALE]
    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE


#this is mine
#input image of rgb and computes new values for each pixel
def rgb2cmyk(pic):
    v,h,d = pic.shape
    new_pic = np.zeros((v, h, 4))
    for i in range(v):
        for j in range(h):
            new_pic[i,j,0], new_pic[i,j,1], new_pic[i,j,2], new_pic[i,j,3] = rgb_to_cmyk(pic[i,j,0], pic[i,j,1], pic[i,j,2])
    return new_pic

#performs needed setup for other functions
#also provides binary edges info
#must use first
def otsu(fname, bname):
    #read in image as bw
    adata = sm.imread(fname, flatten=False)
    #convert rgb to cmyk color space
    adata_new = rgb2cmyk(adata)
    ###########################
    #Max Convolution
    ###########################
    adata_smo = nd.maximum_filter(adata_new[:,:,2], size=3)
    #from https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_equalize.html
    ###########################
    #Contrast stretching
    ###########################
    p2, p98 = np.percentile(adata_smo, (2, 98))
    img_rescale = exposure.rescale_intensity(adata_smo, in_range=(p2, p98))
    #from https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_equalize.html
    ###########################
    #Histogram Equalization
    ###########################
    img_eq = exposure.equalize_hist(adata_smo)
    ###########################
    #Combine Images
    ###########################
    adata_ultima = (2*img_rescale) + img_eq
    ###########################
    #Apply Otsu on Combined Images
    ###########################
    val = filters.threshold_otsu(adata_ultima)
    bdata = adata_ultima < val
    edg = bdata + 0.0
    ##################
    #erode shape
    ###################
    #pic = (nd.binary_erosion(edg , iterations=1))+0.0
    ##################
    #get largest shape
    ###################
    #b, n = nd.label((pic>0.0)+0.0)
    #finding biggest shapes (except 0s)
    #simp = np.hstack(b)
    #locs= np.nonzero( simp )
    #counts=np.bincount(simp [locs] )
    #vals=counts.argsort()[-3:][::-1]
    #clist = list(map(lambda x: b==x, (0,vals[0]) ))
    #shape = (clist[1]+0)
    #################################
    #get shape closest to the center
    #################################
    pic = edg + 0.0
    b, n = nd.label((pic>0.0)+0.0)
    #finding center of image
    v, h = pic.shape
    #creating distance reference image
    z = np.ones((v,h))+0
    z[v//2,h//2] = 0
    dist = nd.distance_transform_edt(z)
    #getting shapes times distance from center of image
    vals = dist*pic
    #finding biggest shapes (except 0s)
    simp = np.hstack(b)
    locs= np.nonzero( simp )
    counts=np.bincount(simp [locs] )
    vals=counts.argsort()[-3:][::-1]
    clist = list(map(lambda x: b==x, (0,vals[0]) ))
    shape = (clist[1]+0)
    sm.imsave(bname+fname[53:-3]+'png', shape+0.0)
    return shape

#performs needed setup for other functions
#segments image based on color
def simp(fname, bname):
    #read in image as bw
    adata = sm.imread(fname, flatten=False)
    #convert rgb to cmyk color space
    adata_new = rgb2cmyk(adata)
    ###########################
    #Max Convolution
    ###########################
    adata_smo = nd.maximum_filter(adata_new[:,:,2], size=5)
    #from https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_equalize.html
    ###########################
    #Contrast stretching
    ###########################
    p2, p98 = np.percentile(adata_smo, (2, 98))
    img_rescale = exposure.rescale_intensity(adata_smo, in_range=(p2, p98))
    #from https://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_equalize.html
    ###########################
    #Histogram Equalization
    ###########################
    img_eq = exposure.equalize_hist(adata_smo)
    ###########################
    #Combine Images
    ###########################
    adata_ultima = (2*img_rescale) + img_eq
    ###########################
    #Apply Simple Thresholding
    ###########################
    bdata = adata_ultima < (adata_ultima.min()+0.01)
    shape = bdata + 0.0
    #################################
    #get shape closest to the center
    #################################
    pic = shape + 0.0
    b, n = nd.label((pic>0.0)+0.0)
    #finding center of image
    v, h = pic.shape
    #creating distance reference image
    z = np.ones((v,h))+0
    z[v//2,h//2] = 0
    dist = nd.distance_transform_edt(z)
    #getting shapes times distance from center of image
    vals = dist*pic
    #finding biggest shapes (except 0s)
    simp = np.hstack(b)
    locs= np.nonzero( simp )
    counts=np.bincount(simp [locs] )
    vals=counts.argsort()[-3:][::-1]
    clist = list(map(lambda x: b==x, (0,vals[0]) ))
    shape = (clist[1]+0)
    sm.imsave(bname+fname[53:-3]+'png', shape+0.0)
    return shape

#performs needed setup for other functions
#segments image using adaptive thresholding
def adapt(fname, bname):
    #read in image as bw
    adata = sm.imread(fname, flatten=True)
    #apply thresholding
    shape  = threshold_adaptive(adata, 20, 5)
    #################################
    #get shape closest to the center
    #################################
    pic = shape + 0.0
    b, n = nd.label((pic>0.0)+0.0)
    #finding center of image
    v, h = pic.shape
    #creating distance reference image
    z = np.ones((v,h))+0
    z[v//2,h//2] = 0
    dist = nd.distance_transform_edt(z)
    #getting shapes times distance from center of image
    vals = dist*pic
    #finding biggest shapes (except 0s)
    simp = np.hstack(b)
    locs= np.nonzero( simp )
    counts=np.bincount(simp [locs] )
    vals=counts.argsort()[-3:][::-1]
    clist = list(map(lambda x: b==x, (0,vals[0]) ))
    shape = (clist[1]+0)
    sm.imsave(bname+fname[53:-3]+'png', shape+0.0)
    return shape

#from Kinser, 2018, texture.py
#calculates the co-occurence matrix
def Cooccurrence (mat, shift, N):
    p = np.zeros((N,N))
    b = nd.shift(mat, shift)
    for i in range(N):
        for j in range(N):
            p[i,j] = ((mat==i)*(b==j)).sum()
    return p

#extract texture metrics; requires shape to be extracted first
def Textures(pic, mask):
    #setup
    texture = np.zeros((1,2))
    #take grayscale image and apply mask
    pic = pic*mask
    #collect co-occrence matrix
    mat = Cooccurrence(pic, 1, 256)
    #extarct mean color for r, g, b
    texture[0][0] = mat.mean()
    texture[0][1] = mat.std()
    return texture

#getting all .pgm's and .png's
def GetPicNames( indir ):
    a = os.listdir( indir )
    pgmnames= []
    for t in a:
        if '.tif' in t:
            pgmnames.append( indir + '/' + t )
        if '.png' in t:
            pgmnames.append( indir + '/' + t )
        if '.jpg' in t:
            pgmnames.append( indir + '/' + t )
        if '.bmp' in t:
            pgmnames.append( indir + '/' + t )
    return pgmnames

#obtaining images
def GetAllImages( dirs, bname ):
    mgs = []
    for d in dirs:
        mgnames = GetPicNames( d )
        for j in mgnames:
            b = convert(j, bname)
            c = enc_circ(b)
            mgs.append( c )
    return mgs

#obtaining images for shape metrics except EIs
def GetAllImages_Shapes( dirs):
    mgs = []
    for d in dirs:
        mgnames = GetPicNames( d )
        for j in mgnames:
            b = sm.imread(j, flatten=True)
            b = (b>125.0) +0.0
            c = Shapes(b)
            mgs.append( c )
    return mgs

#obtaining images for color metrics
def GetAllImages_Colors( dirs, og):
    mgs = []
    d = dirs[0]
    mgnames = GetPicNames( d)
    for j in mgnames:
        #read in mask
        b = sm.imread(j, flatten=True)
        b = (b>125.0) +0.0
        #read in original image
        d = sm.imread(og[0]+j[12:-4]+'.tif', flatten=False)
        #extract color metrics
        c = Colors(d, b)
        mgs.append( c )
    return mgs

#obtaining images for shape metrics except EIs
def GetAllImages_Texture( dirs, og):
    mgs = []
    d = dirs[0]
    mgnames = GetPicNames( d)
    for j in mgnames:
        #read in mask
        b = sm.imread(j, flatten=True)
        b = (b>125.0) +0.0
        #read in original image
        d = sm.imread(og[0]+j[12:-4]+'.tif', flatten=True)
        #extract texture metrics
        c = Textures(d, b)
        mgs.append( c )
    return mgs

#histogram conversion for 256 intensities.
def GSHistogram(dirs, bname):
    imgs = []
    imgs.append(GetAllImages(dirs, bname)) #images obtained from directory
    hist = np.zeros( (len(imgs[0]),2) )
    #get histogram values
    for i in range(0,(len(imgs[0]))):
        temp = imgs[0][i].ravel()
        temp = (temp < 256/2) + 0
        hist[i] = np.array(np.histogram(temp, bins=range(0, 3))[0])
    #return vals
    return hist

#gets binary image histogram
def BinaryHist(dirs, bname):
    imgs = []
    imgs.append(GetAllImages(dirs, bname))
    hist = np.zeros( (len(imgs[0]),2) )
    #get histogram values
    for i in range(0,(len(imgs[0]))):
        hist[i][0] = imgs[0][i].sum()
        hist[i][1] = (imgs[0][i].shape[0]*imgs[0][i].shape[1]) - hist[i][0]
    #return vals
    return hist

#save histogram as .txt where first column is white counts
#and second column is black counts
def BinaryHistTXT(tname, dirs, bname):
    #obtain histogram
    hist = BinaryHist(dirs, bname)
    #get image names
    names = GetPicNames( dirs[0] )
    #save as txt
    np.savetxt(tname, hist, delimiter=',', header="white,black", comments='')
    np.savetxt("NAMES_"+tname, np.asarray(names), delimiter=',', header="image", comments='', fmt="%s")

#save histogram as .txt where first column is white counts
#and second column is black counts
def BinaryShapesTXT(tname, dirs):
    #obtain shape metrics
    shapes = GetAllImages_Shapes(dirs)
    #get image names
    name6 = tname + "_SHAPES.txt"
    #save as txt
    np.savetxt(name6, np.vstack(shapes), delimiter=',', header="Shape_circ, Shape_eccent, Shape_e1, Shape_e2, Shape_corn, White_box, Black_box, Hu1, Hu2, Hu3, Hu4, Hu5, Hu6, Hu7", comments='')

#save color metrics .txt
def BinaryColorTXT(tname, dirs, og):
    #obtain shape metrics
    colors = GetAllImages_Colors(dirs, og)
    #get image names
    name = tname + "_COLORS.txt"
    #save as txt
    np.savetxt(name, np.vstack(colors), delimiter=',', header="Mean_R, SD_R, Mean_G, SD_G, Mean_B, SD_B, Mean_C, SD_C, Mean_M, SD_M, Mean_Y, SD_Y, Mean_K, SD_K", comments='')

#save texture metrics .txt
def BinaryTextureTXT(tname, dirs, og):
    #obtain shape metrics
    colors = GetAllImages_Texture(dirs, og)
    #get image names
    name = tname + "_TEXTURE.txt"
    #save as txt
    np.savetxt(name, np.vstack(colors), delimiter=',', header="Mean_P, SD_P", comments='')

#
