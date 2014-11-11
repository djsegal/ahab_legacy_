# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:11:24 2013

@author: dan
"""

from readInteger         import readInteger
from readReal            import readReal
from ahabSyntax          import incrementChars   ,   floatChars
from ahabErrorMessages   import err0

def readValue( curLine , givenFloatStatus ):
    
    # ==================================
    #  allow simple input to go through 
    #    quickly (i.e. no inc chars )
    # ==================================

    if not any(         x1 in y1 
                    for x1 in incrementChars 
                    for y1 in curLine           ) :

        if not any(     x2 in y2 
                    for x2 in floatChars 
                    for y2 in curLine           ) :
                        
            return map( int   , curLine )
                        
        else :
            
            return map( float , curLine )

    # ========================================     
    #  find special character used in curLine
    # ========================================
    
    curChar = []
    
    for part in curLine :
                
        for ( j , incChar ) in enumerate( incrementChars ) :
            
            if incChar in part :    # an incChar found
                
                if curChar == [] :
                    
                    curMode = j + 1
                    curChar = incChar
                    
                    break
                    
                else :
                    
                    # -------------------------------------
                    #  if two different inc chars are used 
                    #    in one line, raise an exception
                    # -------------------------------------
                    
                    if curChar != incChar :
                        
                        raise Exception( err0 ) 
                        
                    else :
                        
                        break
                    
    # ==================
    #  recreate curline
    # ==================
        
    tmpLine = []            
    
    while curLine != [] :
                
        tmpValues = curLine.pop(0)
        
        if curChar  in  tmpValues :
            tmpValues = tmpValues.split(curChar)

        tmpValues   = filter(lambda a: a !=   ''    , tmpValues ) 
        tmpValues   = filter(lambda a: a != curChar , tmpValues )
        
        if not tmpValues:
            
            continue
                
        if isinstance(tmpValues, list):

            for i in range(len(tmpValues)):
                
                curLine.insert(i,tmpValues[i])
    
        else :
            
            tmpValues = tmpValues.split(curChar)
            
            if tmpValues[0][ 0] == curChar:
                
                tmpValues = tmpValues[0][2:-1]
                
            if tmpValues[0][-1] == curChar:
                
                tmpValues = tmpValues[0][1:-2]       

            tmpLine.append(tmpValues)       
                        
    curLine = [item for sublist in tmpLine for item in sublist]
    
    # ==================================
    #  make a list of all the curValues 
    #   defined by curLine and curMode
    # ==================================  

    # -------------------------------------
    #     transform curLine to list of 
    #  nums (floats or ints) and return it
    # -------------------------------------         
        
    if givenFloatStatus == 1  or any (       fltChr in aLine 
                                         for fltChr in floatChars 
                                         for aLine  in curLine     ) :


        curValues  =  readReal(                 curMode   ,  
                                       map(     float     ,  curLine )  ) 
                                    
                                             
    else :
    
    
        curValues  =  readInteger(              curMode   ,   
                                       map(     int       ,  curLine )  )
                                    
                
    return curValues
    