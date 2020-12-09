# -*- coding: utf-8 -*-
"""
Spyder Editor
Parsing the Motion log
"""
import datetime
pathd = "/Users/davidmoore/Downloads/e2eSensorNetwork-master/motion/"
filed = "motion2.log"
evtStatus = False
full_path = pathd+filed
camera = filed.split(".")[0]
evtStart = ""
evtEnd = ""
fileName = ""
year = "2020"
records = []
import pickle

def dateClean(dateString):
    date_time_obj = datetime.datetime.strptime(dateString, '%Y %b %d %H:%M:%S')
    return date_time_obj    


with open(full_path) as f:
    lines = [line.rstrip() for line in f]
    
for line in lines:
    components = line.replace("[","").split("]")
    
    if (evtStatus == True):
        if (len(components) > 3):
            if (components[2].strip(" ") == "ALL"): 
                if ("End of event" in components[4] ):
                    evtEndD = components[3].strip(" ")
                    evtEnd= dateClean(year+" "+evtEndD)
                    evtStatus = False
                    delta = evtEnd - evtStart
                    mins = int(delta.total_seconds() / 60)
                    rec = {"Camera": camera,
                           "StartEvent": evtStart,
                           "EndEvent": evtEnd,
                           "FileName": fileName,
                           "DurMins": mins}
                    records.append(rec)   
                    evtStart = ""
                    evtEnd = ""
                    fileName = ""
    
    else:    
       if (len(components) > 3):
            if (components[2].strip(" ") == "EVT"):
                evtStatus = True
                evtStartD = components[3].strip(" ")
                fileName = components[4].split(":")[2].strip()
                try:
                    year = fileName.split("/")[5].split("-")[1][:4]
                except:
                    year = "2020"
                evtStart = dateClean(year+" "+evtStartD)

 

with open(pathd+"anal", "wb") as f:
    pickle.dump(records, f, pickle.HIGHEST_PROTOCOL)

   
    
    