# -*- coding: utf-8 -*-
"""
Created on Fri May 30 23:43:50 2014

@author: dan
"""

from ahabSyntax  import constChar , openingChars , closingChars

from readValue   import readValue
from readVector  import readVector

def addScalarInput( curLine , varList , valuesList , constsList , vectorList ):

    # --------------    
    #  index of '<'  
    # --------------

    indepIndex =  len(   openingChars    )  -  1     

    # -----------------------------------------------------------
    #   NOTE : Constants are not allowed to depend on constants      
    #     if they were, this section would have to be changed
    #    for one, the '@'s need deleting --> varList.pop()[1:-1]
    #       ( ^ this was changed , but you get the idea ^ )
    # -----------------------------------------------------------
    
    if any( constChar in linePart for linePart in curLine ) :
        
        equivVectorLine = ( [ openingChars[indepIndex] ] + curLine 
        
                        +   [ closingChars[indepIndex] ] )    
                
        ( curValues , curTypes ) = readVector( equivVectorLine , constsList )

        vectorList.append(   ( varList.pop() , curValues , curTypes )   )
        
        return
        
    # -------------------------    
    #  add a scalar input that 
    #  doesn't have a constant
    # -------------------------
    
    curValues = readValue( curLine , 0 )                
    
    if not constChar in varList[-1] :
        
        valuesList.append( curValues )  
        
    else:
        
        constsList[ varList.pop().lower()[1:-1] ]  =  curValues
    
    return
    