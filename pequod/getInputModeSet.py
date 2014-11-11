# -*- coding: utf-8 -*-
"""
Created on Thu May 29 12:31:55 2014

@author: dan
"""

def getInputModeSet( inputModes , constDepends , indepIndex , constNames ) :

    # ----------------------------------------
    #  remove redundancies from the mode list
    # ----------------------------------------

    inputModeSet  =  list(  set( inputModes )  )

    # -------------------------------------    
    #  remove 'just consts' modes from set 
    #             then add consts  to  set
    # -------------------------------------

    if -5 in inputModeSet :
        
        inputModeSet.pop(  inputModeSet.index(     -5     )  )
                       
    for aConst in set(  [   
                                item for sublist in constDepends 
                                     for item    in sublist            
                        ]  ) :
        
        inputModeSet.append(   -10  *  (  1 + constNames.index( aConst )  )   )
                                  
    # --------------------------- 
    #  mark indep vars for later
    # ---------------------------

    indepCount    =  inputModes.count( indepIndex )
    
    if indepCount > 0 :
        
        inputModeSet.pop(  inputModeSet.index( indepIndex )  )
        
        # -------------------------------------        
        #  -2 is a marker, it later becomes -1
        # -------------------------------------
        
        inputModeSet += [ -2 ] * indepCount  
        
    return inputModeSet