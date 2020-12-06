#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from moviepy.editor import VideoFileClip, concatenate_videoclips
import glob
import os
from datetime import date
import time
today = str(date.today())
import datetime
now = str(datetime.datetime.now())
now = now.replace(' ','_').replace(':','_')

import pickle

def convert_unit(size_in_bytes, unit):
   """ Convert the size from bytes to other units like KB, MB or GB"""
   if unit == 'KB':
       return size_in_bytes/1024
   elif unit == 'MB':
       return size_in_bytes/(1024*1024)
   elif unit == 'GB':
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes
  

vids = (glob.glob("/Users/davidmoore/Downloads/e2eSensorNetwork-master/Monitor2/*.mkv"))
vids2 = (glob.glob("/Users/davidmoore/Downloads/e2eSensorNetwork-master/Monitor/*.mkv"))
vids3 = (glob.glob("/Users/davidmoore/Downloads/e2eSensorNetwork-master/Monitor3/*.mkv"))
vids4 = (glob.glob("/Users/davidmoore/Downloads/e2eSensorNetwork-master/Monitor4/*.mkv"))
vids5 = (glob.glob("/Users/davidmoore/Downloads/e2eSensorNetwork-master/Monitor5/*.mkv"))
vids6 = (glob.glob("/Users/davidmoore/Downloads/e2eSensorNetwork-master/Monitor6/*.mkv"))

vids  = sorted(vids,  reverse=False)
vids2 = sorted(vids2, reverse=False)
vids3 = sorted(vids3, reverse=False)
vids4 = sorted(vids4, reverse=False)
vids5 = sorted(vids5, reverse=False)
vids6 = sorted(vids6, reverse=False)

if ((len(vids) + len(vids2) + len(vids3) + len(vids4)) > 0):
    time.sleep(3)

    vid_list = []
    
    if (len(vids) > 0):
        for vid in vids:
           try: 
            clip = VideoFileClip(vid)
            vid_list.append(clip)
           except:
            continue
        
    if (len(vids5) > 0):
        for vid in vids5:
           try: 
            clip = VideoFileClip(vid)
            vid_list.append(clip)
           except:
            continue        
        
    if (len(vids6) > 0):
        for vid in vids6:
           try: 
            clip = VideoFileClip(vid)
            vid_list.append(clip)
           except:
            continue
 
 
    if (len(vids2) > 0):
        for vid in vids2:
           try: 
            clip = VideoFileClip(vid)
            vid_list.append(clip)
           except:
            continue  

    if (len(vids3) > 0):
        for vid in vids3:
           try: 
            clip = VideoFileClip(vid)
            vid_list.append(clip)
           except:
            continue   

    if (len(vids4) > 0):
        for vid in vids4:
           try: 
            clip = VideoFileClip(vid)
            vid_list.append(clip)
           except:
            continue         
   
    if (len(vid_list) > 0):
        full_vid = concatenate_videoclips(vid_list)
        out_file = f"/Users/davidmoore/Downloads/e2eSensorNetwork-master/archives/{now}_con.mp4"
        full_vid.write_videofile(out_file)

        for vid in vids:
            os.remove(vid)
    
        for vid in vids2:
            os.remove(vid)
        
        for vid in vids3:
            os.remove(vid)      
     
        for vid in vids4:
            os.remove(vid)
            
        for vid in vids5:
            os.remove(vid)

        for vid in vids6:
            os.remove(vid)


else:
    print('nothing')        
   



