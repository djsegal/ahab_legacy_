# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:43:28 2014

@author: dan
"""

from readVector import readVector

from ahabErrorMessages import err6

def addVectorInput(  vectorLine  ,  constsList  ,  vectorList  , 
                     curName     ,  andFound    ,  varList     )  :
    
    # ------------------------------------------------                
    #  read vector line and add it to the vector list
    # ------------------------------------------------
    
    if vectorLine:
        
        vectorLine = [item for sublist in vectorLine for item in sublist]
        
        ( curValues , curTypes ) = readVector( vectorLine , constsList )

        vectorList.append( ( curName , curValues , curTypes ) )

    else:
        
        raise Exception( err6 ) 
    
    # ------------------------
    #  update isVector status
    # ------------------------           
    
    if not andFound :
        
        isVector       =  False
        
    else:
        
        isVector       =  True
        varList.append(curName)
        
    return isVector