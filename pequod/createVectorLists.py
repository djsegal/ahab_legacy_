# -*- coding: utf-8 -*-
"""
Created on Fri May 30 19:52:46 2014

@author: dan
"""

from  getMultiCurVals      import           getMultiCurVals
from  readCurVectorInput   import           readCurVectorInput
from  readValue            import           readValue

from  copy                 import           deepcopy

def   createVectorLists(   standardVals  ,  inputValues         ,
                           inputModes    ,  inputModeSet        ,
                           constsList    ,  constDependences    ,
                           indepIndex    ,  isFloat             )  : 
     
    # =========================================
    #  create the vectorLists   --- AND --- 
    #    the vectorTypes that will be returned
    #     as well as a variables that help it
    # =========================================

    returnLists     =  [ [ ] ]
    
    returnTypes     =  [ [0] * len( inputModeSet ) ]

    deleteIndices   =    [ ]    
 
    for runOfStdVals in standardVals  :
        
        # ====================================
        #  check for runOfStdVal's existence,
        #       then add all of its vals 
        #      to the entire set of lists
        # ====================================
        
        if runOfStdVals:
            
            for curVal in runOfStdVals :
                
                for j in range(  len( returnLists )  ) :
    
                    returnLists[j].append( curVal )  
            
        # ======================================
        #  continue over empty inputValue lists
        # ======================================
            
        if inputValues == [] :
            
            continue 
     
        # =================================================
        #  because the pairing between the number of lists
        #   is one-to-one or off-by-one in stdVals' favor,
        #   current input information is just popped off
        # =================================================
     
        curDeps    =     constDependences.pop(0)           
        curVals    =          inputValues.pop(0)
        curMode    =           inputModes.pop(0)
                
        # ===================================================
        #  get all possible combinations of the consts vals.
        #    if there aren't any consts, create a variable 
        #      so that the algorithm still works for them
        # ===================================================
      
        (  multiCurVals  ,  curTypesList  ,  curConstModes  )   =   \
                                             getMultiCurVals(       \
           curVals       ,  curDeps       ,  constsList     )    
                  
        # ========================================
        #  create new returnLists and returnTypes
        # ========================================
                  
                                                      #------------------------
        oldReturnLists  =  deepcopy( returnLists )    #    make a deepcopy
        oldReturnTypes  =  deepcopy( returnTypes )    #  of the original vars
                                                      #------------------------
        returnLists     =  []                         # reset the vars so that
        returnTypes     =  []                         #   they can be rebuilt
                                                      #------------------------        
        stopChange      =  False                      #   prep for if there  
        curModeList     =  [curMode] + curConstModes  #  are vecs with consts
                                                      #------------------------   
        
        # -----------------------------------       
        #  loop through multiCurVals.
        #  note : for vecs without cons, 
        #         there's only one iteration
        # -----------------------------------
        
        for ( i , aCurVals ) in enumerate ( multiCurVals ) :

            # -------------------------------------                        
            #  read in values for the curValueList
            # -------------------------------------
                        
            curValueList = readValue( [''.join(aCurVals)] , isFloat )

            # ------------------------------------------            
            #  ( 1 ) make a copy of the old return vars
            #  ( 2 ) get tmp return vars using aCurVals
            #  ( 3 ) add a copy of them to the new vars 
            # ------------------------------------------
            
            curReturnLists = deepcopy( oldReturnLists )
            curReturnTypes = deepcopy( oldReturnTypes )
                                 
            curDeleteIndices     =   readCurVectorInput(    
                curReturnLists   ,   curReturnTypes    ,       
                curModeList      ,   curValueList      ,  
                inputModeSet     ,   curTypesList[i]   ,
                stopChange       )
                
            returnLists   += deepcopy( curReturnLists )
            returnTypes   += deepcopy( curReturnTypes )  
            
            # ---------------------------------
            #    only change the indep index  
            #  once inside readCurVectorInputs 
            # ---------------------------------
            
            if not stopChange and curMode == indepIndex :
            
                stopChange = True

        # ------------------------------------                             
        #  update the list of deleted indices
        #  with the ones from the recent call
        #       to readCurVectorInput
        # ------------------------------------
                             
        deleteIndices += curDeleteIndices
    
    # -----------------------------------------------------------
    #  don't include types that have: one element length vectors
    #                            or arent meant to be swept over 
    # -----------------------------------------------------------

    for curType in reversed(   list(  set( deleteIndices )  )   ) :
        
        inputModeSet.pop(curType)
        
        for i in range(len(returnTypes)):
            
            returnTypes[i].pop(curType)    
        
    return ( returnLists , returnTypes )