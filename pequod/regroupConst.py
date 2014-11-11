# -*- coding: utf-8 -*-
"""
Created on Wed May 28 03:29:55 2014

@author: dan
"""

from ahabSyntax          import constChar , openingChars , closingChars 

from regroupConstHelper  import regroupConstHelper

from ahabErrorMessages   import err2

def regroupConst( curLine ) :

    # =======================
    #  build up equationInfo
    # =======================

    equationInfo  =  [] 
    tmpStartInd   =  -1

    for ( i , aPart ) in enumerate( curLine )  :
                              
        if constChar in aPart :
            
            checkInd = 1 + aPart.index( constChar )
            
            if aPart[ checkInd ] not in openingChars :
             
                # -----------------------------
                #  for standardizing purposes, 
                #   wrap constants in @ signs
                #    i.e.    @a   -->   @a@    
                # -----------------------------                      
          
                curLine[i] = curLine[i].lower() + constChar 
                
                #  ======================================         
                #    ^ note : curLine[i] equals aPart ^
                #  ======================================  
                
            else:
                
                tmpStartInd = i
                
                if aPart[checkInd] == '(' :
                
                    raise Exception( err2 )               
                
                else:
                    
                    # -----------------------------------
                    #  variable we're on the lookout for
                    # -----------------------------------
                    
                    charIndex   = openingChars.index(aPart[checkInd])
                    lookOutChar = closingChars[charIndex]
                
        if tmpStartInd != -1 and lookOutChar in curLine[i] :
            
            equationInfo.append( [ tmpStartInd , ( i - tmpStartInd ) ] )
            
            tmpStartInd = -1

    # ==========================================
    #        for each const in the line:
    #   first , merge const into a single word
    #  second , send word to regroupConstHelper 
    #           in order to update the line       
    # ==========================================
    
    for curIndices in reversed(equationInfo) :
                
        mergedWord = ''            
        
        for j in range( 1 + curIndices[1] ):
            
            mergedWord += curLine.pop( curIndices[0] )

        regroupConstHelper( mergedWord , curLine , curIndices )
                    