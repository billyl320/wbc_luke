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

#part 1
all = ["/home/billy/Documents/Research/data/C-NMC_Leukemia/al1", "none"]
binary = 'data_binary/'

#name of .txt file
name = 'al1.txt'

#converting images
#cvt.BinaryHistTXT(name, all, binary)
cvt.BinaryShapesTXT(name[-0:-4], [binary+all[0][51:]] )
cvt.BinaryColorTXT(name[-0:-4], [binary+all[0][51:]],[all[0][0:51]] )
cvt.BinaryTextureTXT(name[-0:-4], [binary+all[0][51:]],[all[0][0:51]] )

#########
#part 2
#########
all = ["/home/billy/Documents/Research/data/C-NMC_Leukemia/al2", "none"]
binary = 'data_binary/'

#name of .txt file
name = 'al2.txt'

#converting images
cvt.BinaryHistTXT(name, all, binary)
cvt.BinaryShapesTXT(name[-0:-4], [binary+all[0][51:]] )
cvt.BinaryColorTXT(name[-0:-4], [binary+all[0][51:]],[all[0][0:51]] )
cvt.BinaryTextureTXT(name[-0:-4], [binary+all[0][51:]],[all[0][0:51]] )

#----------------------------------------------------------
#hem class

hem = ["/home/billy/Documents/Research/data/C-NMC_Leukemia/hem", "none"]
binary = 'data_binary/'

#name of .txt file
name = 'hem.txt'

#converting images
#cvt.BinaryHistTXT(name, hem, binary)
#cvt.BinaryShapesTXT(name[-0:-4], [binary+hem[0][51:]] )
#cvt.BinaryColorTXT(name[-0:-4], [binary+hem[0][51:]], [hem[0][0:51]]  )
#cvt.BinaryTextureTXT(name[-0:-4], [binary+hem[0][51:]], [hem[0][0:51]]  )
#----------------------------------------------------------
