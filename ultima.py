#converting images for analysis in R
#importing custom module for analysis
import convert as cvt

#desired directories
#note that each class should be separated into different directories.
#however, for the fucntion to work, multiple directories should be specified.
#thus, an empty folder is utilized for this task
#the empty folder is called "none"

#----------------------------------------------------------
#all class

all = ["/home/billy/Documents/Research/data/all_idb/all_idb2_all", "none"]
binary = 'data_binary/'

#name of .txt file
name = 'all.txt'

#converting images
cvt.BinaryHistTXT(name, all, binary)
cvt.BinaryShapesTXT(name[-0:-4], [binary+all[0][53:]] )
cvt.BinaryColorTXT(name[-0:-4],  [binary+all[0][53:]],[all[0][0:53]] )
cvt.BinaryTextureTXT(name[-0:-4],  [binary+all[0][53:]],[all[0][0:53]] )
#----------------------------------------------------------
#hem class

hem = ["/home/billy/Documents/Research/data/all_idb/all_idb2_hem", "none"]
binary = 'data_binary/'

#name of .txt file
name = 'hem.txt'

#converting images
cvt.BinaryHistTXT(name, hem, binary)
cvt.BinaryShapesTXT(name[-0:-4], [binary+hem[0][53:]] )
cvt.BinaryColorTXT(name[-0:-4],  [binary+hem[0][53:]], [hem[0][0:53]] )
cvt.BinaryTextureTXT(name[-0:-4],  [binary+hem[0][53:]], [hem[0][0:53]] )
#----------------------------------------------------------
