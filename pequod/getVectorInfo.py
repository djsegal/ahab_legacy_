# -*- coding: utf-8 -*-
"""
Created on Sat May 24 03:40:48 2014

@author: dan
"""

from ahabSyntax      import constChar , floatChars

def getVectorInfo( standardVals , inputValues , inputModes ):
    
    # ======================================
    #  find out if the vector has constants 
    # ======================================
    
    hasConsts  =  (     # doo da dooo   ,   white space
            any( constChar in j for k in standardVals for j in k ) or 
            any( constChar in j for k in inputValues  for j in k ) ) 
            
    # ================================================ 
    #   find the float status for the given vectors
    # ------------------------------------------------
    #  <> for vecs w/  consts:  only check stdVars
    #                           inpVars are checked
    #                           in getConstDeps()
    #  <> for vecs w/o consts: 
    #                find the definitive float status              
    # ================================================
            
    if hasConsts :
        
        isFloat = any( curChar in j for curChar in floatChars  # say this three
                         for k in standardVals for j in k )    #   times fast
                         
    else:
        
        isFloat = (  any( curChar in j for curChar in floatChars 
                            for k in standardVals for j in k )  or 
                     any( curChar in j for curChar in floatChars 
                            for k in inputValues  for j in k )   )
                                
    # -------------------------------------------------
    #  return the float status and the const status
    #   if the vector has consts, 
    #    <> the float status is partial  === AND ===
    #    <> is completed with getConstantDepenedencies
    # -------------------------------------------------
        
    return ( isFloat , hasConsts )     
        
