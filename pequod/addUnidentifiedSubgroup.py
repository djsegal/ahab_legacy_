# -*- coding: utf-8 -*-
"""
Created on Fri May 30 16:21:32 2014

@author: dan
"""

def addUnidentifiedSubgroup(  curVal        ,  markedChar  ,
                              standardVals  ,  curStdVals  , 
                              inputValues   ,  curInpVals  )  :    

    openSubgroup  =  True  #  subgroup is still open
                          
    # ---------------------            
    #  build up curInpVals
    # ---------------------
    
    for aVal in curVal.split( markedChar ) :
        
        if aVal != '' :
        
            curInpVals.append( aVal )

    # --------------------------------            
    #  check if subgroup is completed
    # --------------------------------
    
    if len( curInpVals ) > 3 :
        
        print 'replace this error message once found'
        
    if len( curInpVals ) == 3 :
                        
        curLine = ( [ curInpVals[0] ] + [ markedChar ] +
                    [ curInpVals[1] ] + [ markedChar ] + 
                    [ curInpVals[2] ] )  

        standardVals.append(  curStdVals  )
        inputValues.append(   curLine     )  
        
        ( curStdVals , curInpVals )  =  ( [] , [] )  
        
        openSubgroup = False
    
    return openSubgroup