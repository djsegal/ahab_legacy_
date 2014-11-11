# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:53:55 2013

@author: dan
"""

from  parseLine          import  parseLine
from  findAndChar        import  findAndChar

from  addScalarInput     import  addScalarInput
from  addVectorInput     import  addVectorInput

def readInput( fileName ):
       
    redInput   =  open(  fileName , 'r'  )
    
    varList    = [] # list of all the variables
    valuesList = [] # list of lists of all variables' values
    constsList = {} # dict that contains consts names (keys) and their values
    vectorList = [] # list of tuples that contain :  vec names  ,  vec vals  ,
                    #                                  and mode information
    
    isVector        =  False
    vectorComplete  =  False
    alreadyNamed    =  False
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  read in red.inp one line at a time
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    for aLine in redInput:

        # =========================
        #  get aLine in a workable 
        #   condition for reading
        # =========================
                        
        curLine = parseLine( aLine )
        
        if curLine == '' :
            
            continue
        
        # ============================
        #  find the name of a var AND 
        #    if it's scalar , add it  
        # ============================
 
        if not isVector:
                                                      
            # -------------------------------
            #  get variable names, if needed
            # -------------------------------
                                    
            if  alreadyNamed  :
            
                alreadyNamed  =  False
                
            else: 
                
                varList.append( curLine.pop(0) )
                
                if len( curLine )  ==  0  :
                    
                    alreadyNamed = True
                                         
                    continue
            
        # =============================
        #  check for new vector inputs
        # =============================
        
        if '[' in curLine[ 0 ] :

            isVector    =  True
            vectorLine  =  [] 
            curName     =  varList.pop()
            
            if '[' == curLine[ 0 ] :
                
                curLine.pop( 0 )
                
            else :
            
                curLine[ 0 ]  =  curLine[ 0 ][ 1 : ]
            
        # =================================
        #    if the variable is a scalar,
        #  add it and skip vector protocol
        # =================================
                 
        if not isVector :
                                         
            addScalarInput(  curLine     ,  varList     ,  valuesList  , 
                             constsList  ,  vectorList  )            

            continue
            
        # =================================
        #  check for the end of the vector
        # =================================
   
        if curLine :
            
            andFound = findAndChar( curLine )
            
            # ----------------------------------
            #      now that andChar is gone,
            #  ']' has to be the very last char
            # ----------------------------------

            if ']' in curLine[-1] : 
                
                vectorComplete = True  
                
                if len(curLine[-1]) > 1:
                    
                    curLine[-1] = curLine[-1][0:len(curLine[-1])-1]
                    
                else:
                    curLine.pop() 

            vectorLine.append(curLine)
            
        # ==============================
        #  if complete , read in vector                
        # ==============================
        
        if  vectorComplete :
                        
            vectorComplete     =  False
            
            isVector = addVectorInput(  vectorLine  ,  constsList  ,  
                                        vectorList  ,  curName     ,  
                                        andFound    ,  varList     )
                                            
    # -------------------------------
    #  close input and return values
    # -------------------------------

    redInput.close() 
    
    return ( varList , valuesList , vectorList )
    
    