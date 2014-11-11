# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:13:55 2013

@author: dan
"""
from  itertools          import  product
from  copy               import  deepcopy

from  ahabErrorMessages  import  err7

def getValueCombinations( varList , valuesList , vectorList ) :
    
    # =============================
    #     add scalar values   -OR-
    #    produce the vars that  
    #  correspond to their absence
    # =============================

    if valuesList :
        
        returnLists  =  [ list(item) for item in list(product(*valuesList)) ]
        returnTypes  =  [ [i] for i in range( 1 , len(returnLists) + 1 ) ]
        returnInfo   =  [ len(returnLists) ]
        
    else :
        
        returnLists  =  [ [] ]
        returnTypes  =  [ [] ]
        returnInfo   =    []   
     
    # ==================================================
    #  transition from scalar section to vector section
    # ==================================================
    
    if vectorList :
        
        if valuesList :
            
            modePool = [ 0 ]
            
        else :
            
            modePool = [   ]
            
    else :
        
        if valuesList :
            
            return
            
        else :
            
            raise Exception( err7 )

    # =============
    #  add vectors 
    # =============
        
    curVector   =       vectorList.pop(0)  
    varList.append(          curVector[0]     )
    modePool.extend(         curVector[2][1]  )
    returnInfo.extend(       curVector[2][2]  )   
    
    returnLists2 , returnTypes2 = deepcopy(returnLists) , deepcopy(returnTypes)
    returnLists  , returnTypes  =          [ ]          ,         [ ]                

    for      i  in  range(  len( curVector[1] )  )  :     
        
        for  j  in  range(  len( returnLists2 )  )  :
                        
            # ----------------------------
            #  get return lists and types
            # ----------------------------
            
            returnLists2[j].append(  curVector[1][   i] )            
            returnTypes2[j].extend(  curVector[2][0][i] )
            
            returnLists.append(deepcopy(returnLists2[j]))  
            returnTypes.append(deepcopy(returnTypes2[j]))  

            # --------------------------           
            #  clean up after ourselves
            # --------------------------
            
            returnLists2[j].pop()

            for k in range( len( curVector[2][0][i] ) ) :
                
                returnTypes2[j].pop()
    

    print''
    print returnLists
    print returnTypes
    print returnInfo
    print modePool
    print ''
#    raise Exception('halt')            
    # =========================
    #  add rest of the vectors
    # =========================

    for curVector in vectorList:
        
        # --------------------------------------
        #  add current vector's name to varList
        # --------------------------------------

        varList.append( curVector[0] ) 

        # ---------------------------------        
        #  make deep copies of return vars
        # ---------------------------------
        
        (            returnLists2    ,            returnTypes2    )  =  (
           deepcopy( returnLists  )  ,  deepcopy( returnTypes  )  )

        # -------------------------------------------------------          
        #  determine which modes are new and which modes are old
        # -------------------------------------------------------   
              
        newModes , oldModes , repeatIndices = [ ] , [ ] , [ ]
        
        for ( i , curMode ) in enumerate( curVector[2][1] ) :
            
            if curMode == -1 or curMode not in modePool :
                
                newModes.append(    i    )
                modePool.append( curMode )
                
                returnInfo.append(  curVector[2][2][i]  )
                
            else :
                
                oldModes.append(    i    )
                
                repeatIndices.append(  modePool.index( curMode )  )
        
        # =============================================                
        #  following method always extends dimensions, 
        #   i.e. it never starts again from scratch
        #   therefore, start with the first value
        # =============================================

        # ---------------------------- 
        #  add first item in new list
        # ---------------------------- 
        
        for ( i , curModes ) in enumerate( curVector[2][0] ) :
                         
            # --------------------------------------            
            #  only completely new vars handled now
            # --------------------------------------
            
            if not all( curModes[aNewMode] for aNewMode in newModes ) :
                
                continue
                    
            # -----------------------------------------
            #  find out which modes match current list
            # ----------------------------------------- 
            
            curMatch = []
            
            for j in range( len(   oldModes  ) ) :
                
                curMatch.append( curModes[ oldModes[j] ] )
                
#            curMatch2 = [ curModes[anIndex] for anIndex in oldModes ]
#            print ('save space' , curMatch , curMatch2)  # test above and replace
                
                
            for j in range( len( returnLists ) ) :
                                
                tmpMatch = []
                
                for k in range( len( repeatIndices ) ) :
                    
                    tmpMatch.append( returnTypes2[j][ repeatIndices[k] ] )
                    
                if tmpMatch != curMatch:
                    
                    continue
                
                returnLists[j].append( curVector[1][i]    )
                
                for k in range( len( newModes ) ) :
                    
                    returnTypes[j].append( curModes[ newModes[k] ] )        
        
        
        
        for ( i , curModes ) in enumerate( curVector[2][0] ) :
            
            allGood = True
            for j in range( len( newModes ) ) :
                if curModes[newModes[j]] != 1:
                    allGood = False
                    break
            if not allGood :
                continue
            
            curMatch = []
            for j in range( len(   oldModes  ) ) :
                curMatch.append( curModes[ oldModes[j] ] )
                
            for j in range( len( returnLists ) ) :
                                
                tmpMatch = []
                
                for k in range( len( repeatIndices ) ) :
                    tmpMatch.append( returnTypes2[j][ repeatIndices[k] ] )
                    
                if tmpMatch != curMatch:
                    continue
                
                returnLists[j].append( curVector[1][i]    )
                for k in range( len( newModes ) ) :
                    returnTypes[j].append( curModes[ newModes[k] ] )

#        raise Exception('hellion')

        # ---------------------------------------
        #  add the rest of the items to the list
        # ---------------------------------------
        
        curMatches = [[1]]
#        print '777s'
        for i in range( len( newModes ) ) :
            
#            print ( 'twinkies',i , len(newModes) , newModes )
            
            matchesList = [ list(item) for item in list(product(*curMatches)) ]

            for curCount in range( 2 , returnInfo[ i - len(newModes) ] + 1 ) :

                for match in matchesList:
                    
                    for j in range( len( curVector[2][0] ) ) :

                        # -------------------------------------------
                        #  make sure that this is the correct vector
                        # -------------------------------------------

                        allGood = True  # assume everything is all good
                        
                        if allGood :
                            if curVector[2][0][j][newModes[i]] != curCount:            
                                allGood = False                                         

                        if allGood :
                            for k in range( i ) :
                                if curVector[2][0][j][newModes[k]] != match[k]:
                                    allGood = False
                                    break
                                
                        if allGood :
                            for k in range( i+1 , len( newModes ) ) :
                                if curVector[2][0][j][newModes[k]] != 1:
                                    allGood = False
                                    break
                            
                        if not allGood :
                            continue
                        
                        
                        
                        curMatch = []
                        for k in range( len(   oldModes   ) ) :
                            curMatch.append( curVector[2][0][j][ oldModes[k] ] )  
                        
                        for k in range( len( returnLists2 ) ) :
                                            
                            tmpMatch = []                           
                            for m in range( len( repeatIndices ) ) :
                                tmpMatch.append( returnTypes2[k][ repeatIndices[m] ] )
                                
                            if tmpMatch != curMatch:
                                continue
                            
                            returnLists2[k].append( curVector[1][j] )   
                            for m in range( len( newModes ) ) :
                                returnTypes2[k].append( curVector[2][0][j][ newModes[m] ] )
        
                    returnLists.extend(deepcopy(returnLists2))
                    returnTypes.extend(deepcopy(returnTypes2))
                     
                    for j in range( len( returnLists2 ) ) :
                        returnLists2[j].pop()
                        for k in range( len(newModes) ) :
                            returnTypes2[j].pop()
                            
            if curMatches == [[1]] :
                curMatches[0].extend(range( 2 , 1 + returnInfo[ i - len(newModes) ] ) )
            else:
                curMatches.append(range( 1 , 1 + returnInfo[ i - len(newModes) ] ) )



#        print ( 'is this it?'  , curVector , modePool , repeatIndices )

#        print(oldModes , newModes , i , newModes )  
        if newModes :              
            oldModes.append( newModes[i] )  

        # TODO : test this by doing a run with no scalar values
        if len( valuesList ) == 0 :
            tmpVal = 0  
        else:
            tmpVal = 1  

        missingValueFound = False
        while not missingValueFound :
            for j in range( len ( repeatIndices ) ) :
                if repeatIndices[j] == tmpVal:
                    tmpVal = tmpVal + 1
                    break
            else:
                repeatIndices.append(tmpVal)
                missingValueFound = True

#    print(len(returnTypes))
#    for asd in returnTypes:
#        print(asd)                                 

#    asdf
    
    return ( varList , returnLists , returnTypes , returnInfo )