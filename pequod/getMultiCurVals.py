# -*- coding: utf-8 -*-
"""
Created on Thu May 29 04:38:57 2014

@author: dan
"""

# ================================================#|
#     ***  used in eval at the end  ***           #|
# ------------------------------------------------#|
                                                  #|
from  math       import  sin  , cos   , tan       #|
from  math       import  exp  , log   , sqrt      #|
from  math       import  ceil , floor             #|
                                                  #|
# ------------------------------------------------#|
#     ***         *********         ***           #|
# ================================================#|

from  ahabSyntax  import  constChar
from  copy        import  deepcopy

def getMultiCurVals( prevCurVal , curDeps , constsList ) :
    
    # -------------------------------------------
    #  named quasi becaues they resemble the way 
    #   inputModes and returnTypes are handled 
    #   in the level above this one , readVector
    # -------------------------------------------
    
    quasiInputModeSet =     [0] * len( curDeps )  
    
    quasiReturnTypes  =  [  [0] * len( curDeps )  ]    
            
    multiCurVals = [ prevCurVal ]

    # -----------------------------------------    
    #  if there aren't any consts, return this 
    #     so that the readVectors algorithm 
    #     still works (basically recast it)
    # -----------------------------------------

    if not curDeps :
        
        return (  multiCurVals  ,  [ [] ] ,  [ ]  )
        
    # --------------------------       
    #  loop over every constant
    # --------------------------
        
    for ( i , aConst ) in enumerate( curDeps ) :  
    
        quasiInputModeSet[i] = ( -10 * ( 1 + 
                                         constsList.keys().index( aConst ) ) )

        multiCurVals2     = deepcopy(multiCurVals)
        multiCurVals      = []    
        
        quasiReturnTypes2 = deepcopy(quasiReturnTypes)
        quasiReturnTypes  = []   
        
        # -----------------------------------------------------
        #  loop over every number in a const's list of numbers .
        # -----------------------------------------------------
        
        for ( j , constVal ) in enumerate( constsList[ aConst ] ) :   
            
            tmpMember     = []
            
            for ( k , member ) in enumerate( multiCurVals2 ) :
                
                tmpVals   = []
                for aVal in member :
                    
                    tmpVals.append( 
                      aVal.replace( aConst, str(constVal)  )  )
                      
                tmpMember.append( tmpVals )
                
                quasiReturnTypes2[k][i] = j
            
            multiCurVals      +=  tmpMember
            
            quasiReturnTypes  +=  deepcopy( quasiReturnTypes2 )
    
    # ---------------------------------------================--
    #  evaluate every term in multiCurVals ,  mathematically
    #          hence, why all those math functions 
    #                 are imported, but never used    
    # ---------------------------------------------------------
    
    for       ( i , member )    in    enumerate( multiCurVals )   :
        
        for   ( j ,  aVal  )    in    enumerate(    member    )   :
        
            if aVal[0] == constChar :
            
                multiCurVals[i][j] = str( eval( aVal[1:-1] ) )
    
    # --------------------------------------------------
    #  this is similar to readVector's return statement 
    # --------------------------------------------------
    
    return (  multiCurVals  ,  quasiReturnTypes  ,  quasiInputModeSet  )
    