# -*- coding: utf-8 -*-
"""
Created on Fri May 30 13:55:14 2014

@author: dan
"""

from ahabSyntax import constChar , incrementChars , openingChars

def checkForSubgroup( curVal     , standardVals , curStdVals , 
                      inputModes , inputValues  , curInpVals ) :

    # =======================================
    #  check if there is an open subgroup, 
    #        if parseVector needs to 
    #           continue after this call
    #       and then find some stuff out  
    #           about unidentified subgroups
    # =======================================

    openSubgroup   =  False
    needsContinue  =  False
    
    markedChar     =  ''     # no index/subgroup has been marked
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  consts are separated from things 
    #   touching them during readInput
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    if constChar in curVal :

        standardVals.append(curStdVals)
        curStdVals = []
        
        inputModes.append(     -5    )
        inputValues.append( [curVal] )  
        
        needsContinue = True
        
        return ( openSubgroup , needsContinue , markedChar ) 
  
    # ====================================
    #  now that consts are taken care of,
    #     move on to finding subgroups
    # ====================================
  
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  check for subgroups defined by opening chars
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
    
    charFound = False 
    
    for ( i , openChar ) in enumerate( openingChars ) :
        
        if openChar in curVal : 
            
            charFound = True
            break
        
    if charFound :
        
        openSubgroup  =  True
        
        inputModes.append(      i       )           
        standardVals.append( curStdVals )
        
        curStdVals = []
        
        # -----------------------------------                       
        #  continue if curVal is just syntax
        # -----------------------------------
                            
        if len(curVal)  <= 1  :
            
            needsContinue = True
            
        else:
            
            curVal = curVal[1:]
            
        return ( openSubgroup , needsContinue , markedChar ) 

    # ==============================================
    #      final check to see if the value is
    #  a standard value or an unidentified subgroup
    # ==============================================

    charFound = False 
    
    for incChar in incrementChars :
        
        if incChar in curVal :
            
            charFound = True 
            break

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #    if a char was not found , 
    #  the val belongs in a std run
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
    if not charFound :
        
        curStdVals.append(curVal)
        needsContinue = True        

        return ( openSubgroup , needsContinue , markedChar ) 
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  handle unidentified subgroups
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         
                        
    curLine = curVal.split( incChar )
    
    # ------------------------------
    #  check for some special cases
    # ------------------------------
    
    if len( curLine ) == 3 : 
    
        standardVals.append(curStdVals)
        curStdVals = []   

        curLine = ( [ curLine[ 0 ] ] + [ incChar ] +
                    [ curLine[ 1 ] ] + [ incChar ] + 
                    [ curLine[ 2 ] ] )
                    
        inputValues.append( curLine )  
        
        needsContinue = True
        
        return ( openSubgroup , needsContinue , markedChar ) 

    elif len( curLine ) > 3 :
        
        print '1:2:3:4... error'

    # -------------------------------------
    #   at this point len(curLine) == 2,
    #  so start by reading the first value
    # -------------------------------------      
   
    if curLine[0] != '' :
        
        curInpVals.append( curLine[0] )                          
        
    else :
        
        if   curStdVals :
            
            tmpVal = curStdVals.pop()
                            
        else :

            curStdVals   =   standardVals.pop()

            tmpVal  = inputValues.pop() 
            
            tmpMode = inputModes.pop()
            
            if tmpMode != -5 :  
                
                # ------------------------------------
                #  -5 is a constant not in a subgroup
                # ------------------------------------
                
                print 'incorrect format error'
                
        curInpVals += tmpVal 

    # ------------------------------------- 
    #  read in second character from split
    # -------------------------------------
        
    if curLine[1] != '' :
        
        curInpVals += curLine[1] 
        
    # -----------------------------------------------
    #  wrap-up unidentified subgroups identification 
    # -----------------------------------------------
                    
    openSubgroup  =  True
    markedChar    =  incChar # from for loop above                        
    needsContinue =  True

    inputModes.append( len(openingChars) - 1 )
            
    return ( openSubgroup , needsContinue , markedChar ) 
      