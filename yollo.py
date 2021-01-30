from myYoloC import myYolo
from datetime import datetime
import pickle

directoryBase = "/home/david/Documents/projects/yolo-object-detection/images/"
directoryList = ['2021-01-22/',
                '2021-01-23/',
                '2021-01-24/',
                '2021-01-25/',
                '2021-01-26/',
                '2021-01-27/']

results = []
ObjDetect = myYolo(device='cuda')

def persist(imgPath,obj):
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    with open(imgPath+"result_"+dt_string+".picke","wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


for dirInst in directoryList:
    pathImg = directoryBase+dirInst
    #print(pathImg)
    ObjDetect.ImgDir(pathImg)
    objs = ObjDetect.run()
    results.append(objs)


#print(results[:1])
persist(directoryBase,results)
