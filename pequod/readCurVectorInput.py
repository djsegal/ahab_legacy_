# -*- coding: utf-8 -*-

from ahabSyntax          import  openingChars
from ahabErrorMessages   import  err1
from copy                import  deepcopy

def readCurVectorInput( returnLists , returnTypes  , curModeList ,  
                        valueList   , inputModeSet , curTypes    ,
                        stopChange  )              :

    # ====================================
    #       get the curIndices and 
    #  determine if the cur part is indep    
    # ====================================
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #     start with the non-first indices 
    #   b/c they can only depend on constants        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    curIndices =  [0] * len( curModeList )
    
    curRange   =  [ float('inf') ] + [ -1 ]  # consts are applied sequentially
    
    numConsts  =  len( curModeList ) - 1             
    
    if numConsts :
        
        for i in range(          1     ,     len( curModeList  ) )  :
            
            curIndices[i]  =  inputModeSet.index( curModeList[i] )
            
            # -----------------------
            #  find new range bounds
            # -----------------------            
            
            if curIndices[i]  <    curRange[0]  :
                
                 curRange[0]  =  curIndices[i]
                
            if curIndices[i]  >    curRange[1]  :
                
                 curRange[1]  =  curIndices[i]
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #         check for dependence:
    #  as of 2014, indep char is equal to '<'
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    indepMode  =  len( openingChars ) - 1    
            
    if curModeList[0] != indepMode :  
      
        # ---------------------------------
        #  if this part is not independent
        #     get its dependent index   
        # ---------------------------------

        curIndices[0]  =  inputModeSet.index( curModeList[0] )
        
    else :  
    
        # ---------------------------------
        #   if this part is independent,
        #     record its information, 
        #  then change it for future reads
        # ---------------------------------
        
        if stopChange :
            
            # ------------------------------------------------------
            #  if consts are used, dont change index more than once
            # ------------------------------------------------------

            for i in reversed(   range(  len( inputModeSet )  )   )  :
                
                if inputModeSet[i] == -1:
                    
                    curIndices[0] = i
                    break
            
        else :  
            
            # -------------------------------------------
            #  !!!  the change that normally happens !!!    
            # -------------------------------------------
            
            curIndices[0]                   =  inputModeSet.index(-2)
            inputModeSet[ curIndices[0] ]   =  -1 
                
    # =====================================================
    #  build up all the returned elements and returns them    
    # =====================================================
 
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  1  ]
    #          horizontal line insertion      
    #  simplest mode where values are just read in
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
    if curModeList[0] == 0 :   #   delimiters  =  '('  and  ')' 

        #  might not need inputModeSet 
#        print 'returnLists , returnTypes  , curModeList , valueList , inputModeSet , curTypes , stopChange'          
#        print ( 'cricket' , returnLists , returnTypes  , curModeList ,  
#                            valueList   , inputModeSet , curTypes    , stopChange  )    
#        print ( 'hasConstDeps' , numConsts , curIndices , returnTypes)

        if numConsts :
            
            if any( returnTypes[curRange[0]:curRange[1]+1] ) :
            
                print 444    
                
#                for ( j , anIndex ) in enumerate( curIndices[1:] ) :
#                    
#                    if returnTypes[-1][ anIndex ] == 0 :
#
#                        for i in range(  len( returnLists )  ) :
#                        
#                            returnTypes[i][ anIndex ]   =  curTypes[j]
#                        
#                    else :
#                        

            
            else: 
                
                for i in range(  len( returnLists )  ) :
                    
                     returnLists[i]  +=  valueList
                     
                     for ( j , anIndex ) in enumerate( curIndices[1:] ) :
                         
                         returnTypes[i][ anIndex ]   =  curTypes[j]
                         
        else:
            
            print 321
            for j in range(  len( returnLists )  ) :
                
                 returnLists[j] += valueList
                
        deleteIndices = [ curIndices[0] ]

        return deleteIndices
                
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  2  ]
    #  insertion when mode already exists in vector
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#    if returnTypes[-1][curIndex] > 0 and curModeList[0] != indepMode :
            
#        if len( valueList ) != ( returnTypes[-1][curIndex] ) :
#            
#            raise Exception( err1 )
#    
#        for j in range(  len( returnLists )  ) :
#            
#            thisType = returnTypes[j][curIndex] - 1
#            returnLists[j].append(valueList[thisType])
            
#        deleteIndices = [ ]  # dont delete any of these indices
#        return deleteIndices

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  3  ]
    #  else: create new lists and fill them
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
#    returnLists2   =  deepcopy(returnLists)
#    returnLists    =  []
#    
#    returnTypes2   =  deepcopy(returnTypes)
#    returnTypes    =  []
#    
#    typeCounter    =  0
    deleteIndices  =  []

#    for curVal in valueList:
#        
#        typeCounter = typeCounter + 1
#        
#        for j in range(len(returnLists2)):
#                        
#            returnTypes2[j][curIndex] = typeCounter
#            returnTypes.append(deepcopy(returnTypes2[j]))
#            
#            returnLists2[j].append(curVal)
#            returnLists.append(deepcopy(returnLists2[j]))
#            returnLists2[j].pop()
#            
#    if len(valueList) == 1 :    # i.e. typeCounter = 1
#        
#        deleteIndices.append(curIndex)

    return  deleteIndices   