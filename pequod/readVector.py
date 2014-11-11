# -*- coding: utf-8 -*-

"""
Created on Wed Jul 31 23:03:21 2013

@author: dan
"""

from  parseVector               import  parseVector
from  getVectorInfo             import  getVectorInfo
from  getConstantDependences    import  getConstantDependences
from  getInputModeSet           import  getInputModeSet
from  createVectorLists         import  createVectorLists

from  ahabSyntax                import  openingChars

def readVector( vectorLine , constsList ):
    

    # =================================
    #  get the vector's necessary info
    # =================================
        
    ( standardVals , inputValues , inputModes )  =  parseVector( 
                                                 #    vectorLine )
      vectorLine                              )  #  -> stdVals , inpVals , mods
     
    
    ( isFloat      , hasConsts                )  =  getVectorInfo( 
                                                 #   stdVals , inpVals , mods )
      standardVals , inputValues , inputModes )  #  -> isFloat , hasConsts
      
      
    ( bonusFloatStatus   ,  constDependences  )  =  getConstantDependences( 
                                                 #    inpVals , constsNames )
      inputValues        ,  constsList.keys() )  #  -> bonusFloat , constDeps


    # ====================================================      
    #  transform standard string data into numerical data 
    #     e.g., a float could be mapped: '4.2' -> 4.2
    # ====================================================

    if isFloat or bonusFloatStatus : 
        
        standardVals = [ [float(aVal) for aVal    in valList      ]
                                      for valList in standardVals ]
        
    else:
         
        standardVals = [ [  int(aVal) for aVal    in valList      ] 
                                      for valList in standardVals ]


    # ===============================
    #  update input mode information
    # ===============================

    indepIndex    =  len(openingChars)  -  1         #   index of '<'

    inputModeSet  =  getInputModeSet(   inputModes   ,   constDependences    , 
                                        indepIndex   ,   constsList.keys()   )
              

    # =========================================
    #  create the vectorLists   --- AND --- 
    #    the vectorTypes that will be returned
    #    as well as two variables that help it
    # =========================================

    (  returnLists   , returnTypes        )   =   createVectorLists(  
       standardVals  ,  inputValues       ,
       inputModes    ,  inputModeSet      ,
       constsList    ,  constDependences  ,
       indepIndex    ,  isFloat           )
                                
    # ----------------------------------------
    #   package info this way for readInput.
    #  kind of sloppy, but it was implemented
    #  a year ago and works, so why change it
    # ----------------------------------------
                                
    return ( returnLists ,                                  \
                                                            \
           ( returnTypes , inputModeSet , returnTypes[-1] ) )
