from os import listdir
from os.path import isfile, isdir, join, dirname, basename, normpath
import numpy as np
database_loc = "D:\\Personal\\College\\Final Year Project\\Database\\"
ext = "abc"

def runLoop():
    #folders = list of all directories 
    folders = [join(database_loc,folder) for folder in listdir(database_loc) if (isdir(join(database_loc,folder)) and (len(basename(folder)) == 8))]
    #print(folders)
    files =[]
    for folder in folders:
        for file in listdir(folder):
            if (isfile(join(folder,file)) and file.endswith('.'+str(ext))):
                   print(join(folder,file))
                   files.append(join(folder,file))

    importer = hou.node("/obj/cloth/alembic_importer")
    
    for file in files:
        print("filename: " + file)
        importer.setParms({"fileName":file})
        print("importing: " + importer.evalParm("fileName"))
        exportCloth(file)
        print("exported: " + importer.evalParm("fileName"))
    
def exportCloth(filename):
    node = hou.node("/obj/cloth/cloth_sim_HDA/")
    frames = 59
    geo = node.geometry()
    num_points = len(geo.points())
    array = np.zeros((6*frames+3,num_points))
    index = 0
    frame = 0
    for frame in range(frames):
        Pindex=0
        hou.setFrame(frame+1)
        for point in geo.points():
            posAtt = geo.findPointAttrib("P")
            velAtt = geo.findPointAttrib("v")
            attrib_count = posAtt.size()
            array[(frame*6):(frame*6)+3,Pindex] = point.attribValue(posAtt)[:]
            array[(frame*6)+3:(frame*6)+6,Pindex] = point.attribValue(velAtt)[:]
            Pindex = Pindex + 1
    
    #save to npy file
    print(filename[0:len(filename)-3] + "npy")
    np.save(filename[0:len(filename)-3] + "npy", array)