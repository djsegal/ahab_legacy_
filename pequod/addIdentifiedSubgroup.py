# -*- coding: utf-8 -*-
"""
Created on Fri May 30 16:31:36 2014

@author: dan
"""

from ahabSyntax      import openingChars , closingChars

def addIdentifiedSubgroup( curVal , inputModes , inputValues , curInpVals) :
    
    openSubgroup  =  True  #  subgroup is still open
    
    if closingChars[inputModes[-1]] not in curVal: 

        # -------------------------------------------------            
        #   allow subGroups that go onto multiple lines,
        #  therefore add those lines, if they arent syntax
        # -------------------------------------------------
         
        if curVal.strip() not in openingChars + closingChars :
            
            curInpVals.append(curVal)
       
    else:
            
        openSubgroup = False
        
        if len(curVal) > 1:
            curVal = curVal[:-1]
            curInpVals.append(curVal)
        
        # ----------------------------------------
        #  remove syntax from first and last term
        # ----------------------------------------
        
        curInpVals[ 0]  =  curInpVals[ 0].strip()
        curInpVals[-1]  =  curInpVals[-1].strip()
                    
        if  curInpVals[ 0][ 0] in openingChars :
                            
            curInpVals[ 0]      = curInpVals[ 0][ 1 :    ]
            
        if  curInpVals[-1][-1] in closingChars :
                            
            curInpVals[-1]      = curInpVals[-1][ 0 : -1 ]
        
        # -----------------------------------
        #  add current stack of input values
        #   to the actual inputValues pile
        # -----------------------------------
        
        inputValues.append(curInpVals)

        curInpVals = []           
        
    return openSubgroup