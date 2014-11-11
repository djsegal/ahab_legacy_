# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:02:54 2013

@author: dan
"""

from os.path        import isdir
from os             import rename, makedirs
from datetime       import datetime

def makeNewRunDir():
    
    # =====================================================
    #  create a directory for every set defined by red.inp
    #    and fill them with their own modified bucky.inp
    # =====================================================
    
    #   use the current date & time to mak a directory name:
    #  YYMMDD-hhmm (Y:year, M:month, D:day, h:hour, m:minute)
    # --------------------------------------------------------
    curTime = str(datetime.now())
    curDir = ( 'data/' + curTime[ 2: 4] + curTime[ 5: 7] + curTime[ 8:10]
             +   '-'   + curTime[11:13] + curTime[14:16] )
    
    #  if someone submits more than one parameter sweep 
    #   a minute, a  different naming scheme is needed
    # --------------------------------------------------
    altDir = curDir + 'a'               # make the 1st alternative dir
    
    if isdir( curDir ):                 # check existence of curDir 
        rename( curDir , altDir )       #    rename the old directory 
        
    if isdir(  altDir ):                # check existence of altDir 
        for i in range(97,123):         #    cycle through alphabet (a-z)
            altDir = curDir + chr(i)    #    get new altDir
            if not isdir( altDir ):     # check existence of altDir 
                curDir = altDir         #    make altDir the curDir  
                break                   #    stop cycling through alphabet
            
    makedirs( curDir )                  # make new directory
    
    return curDir