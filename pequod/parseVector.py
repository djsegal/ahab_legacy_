# -*- coding: utf-8 -*-
"""
Created on Sat May 24 02:41:20 2014

@author: dan
"""

from checkForSubgroup         import checkForSubgroup
from addUnidentifiedSubgroup  import  addUnidentifiedSubgroup
from   addIdentifiedSubgroup  import    addIdentifiedSubgroup

def parseVector( vectorLine ):
    
    # ===========================================================
    #    think of it like shuffling a deck of cards that starts 
    #   and ends with same stack [where std layers can be empty]
    #   ( standard , input , standard , ... , input , standard )
    # ===========================================================
    
    curStdVals      =  []
    standardVals    =  []
    curInpVals      =  []
    inputValues     =  []
    inputModes      =  []
    
    openSubgroup    =  False     # don't assume vector starts with subGroup 
    
    for curVal in vectorLine:

        if not openSubgroup :
            
            (    openSubgroup , needsContinue  , 
                  markedChar  )                =   checkForSubgroup( curVal , 
                  standardVals , curStdVals     , 
                  inputModes   , inputValues    ,   curInpVals      )
                
        if needsContinue:
            
            needsContinue = False
            
            continue

        # =============================                          
        #  take care of open subgroups
        # =============================

        if markedChar :
                
            openSubgroup = addUnidentifiedSubgroup( curVal       , markedChar ,
                                                    standardVals , curStdVals , 
                                                    inputValues  , curInpVals )

                                
        else : 

            openSubgroup =   addIdentifiedSubgroup( curVal       , inputModes ,
                                                    inputValues  , curInpVals )

    # ----------------------------------------------
    #   if the last thing added to the stack was 
    #  a std vals, put it in the main std vals pile
    # ----------------------------------------------
        
    if curStdVals : 
        
        standardVals.append(curStdVals) 
        
    return( standardVals , inputValues , inputModes )