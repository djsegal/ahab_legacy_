# -*- coding: utf-8 -*-
"""
Created on Fri May 30 22:33:16 2014

@author: dan
"""

from ahabSyntax  import constChar , incrementChars , openingChars , closingChars

from math        import fmod

def regroupConstHelper( mergedWord , curLine , curIndices ) :
    
    # ================================
    #     bug lasted for 5 hours... 
    #  resplitting may not be elegant, 
    #           but it works
    # =================================
    
    offset  =  0
    
    for ( j , curPart ) in enumerate( mergedWord.split(constChar) ) :
        
        if not curPart:
            
            offset -= 1
            continue                
        
        if int(fmod(j,2)) == 0 :
                                
            for incChar in incrementChars:
                
                if incChar in curPart:
                    
                    splitCurPart = curPart.split( incChar )

                    if splitCurPart == [ '' , '' ] :

                        curLine.insert( curIndices[0] 
                                            + j + offset , incChar )
                        offset += 1
                        
                    else:

                        for bit in splitCurPart :
                            
                            curLine.insert( curIndices[0] + 
                                                j + offset , incChar )
                            offset += 1
                     
                            if bit :
                                                                        
                                curLine.insert( curIndices[0] + 
                                                    j + offset , bit )    
                                offset += 1
                                                
                        if splitCurPart[0] :
                            
                            curLine.pop( curIndices[0] - 2 +
                                         j + offset - len(splitCurPart) ) 
                            offset -= 1
                    
                    curLine.pop( curIndices[0] + j + offset - 1 )
                    offset -= 1
                    
                    break
                
            else:
                
                curLine.insert( curIndices[0] + j + offset , curPart )
            
        else :

            # ------------------------------------------------
            #  three values are needed to know a combination.
            #  leftInd2 is arbitrarily chosen over rightInd2.
            # ------------------------------------------------

            ( leftIndex , rightIndex , leftIndex2 )  =  ( -1 , -1 , -1 )
            
            if curPart[ 0] in openingChars:
                
                leftIndex  =  openingChars.index(curPart[ 0])

            if curPart[-1] in closingChars:
                
                rightIndex =  closingChars.index(curPart[-1])
  
            if curPart[ 1] in openingChars:
                
                leftIndex2 =  openingChars.index(curPart[ 1])
                
            # -------------------------------------------
            #  using the indices information from above,
            #          the curLine is corrected
            # -------------------------------------------

            if leftIndex == rightIndex:  
                
                # ++++++++++++++++++++++++++++++++
                #  assume they dont both equal -1
                # ++++++++++++++++++++++++++++++++
                
                curStr = constChar + curPart[1:-1].lower() + constChar
                
                curLine.insert( curIndices[0] + j + offset , curStr )
            
            elif leftIndex2 != -1 and leftIndex2 == rightIndex:
                
                curStr = constChar + curPart[2:-1].lower() + constChar                        
                
                curLine.insert( curIndices[0] + j + offset , curPart[ 0])
                    
                offset += 1
                
                curLine.insert( curIndices[0] + j + offset , curStr )
                
            else: # rightIndex2 != -1 and rightIndex2 == leftIndex:
                
                curStr = constChar + curPart[1:-2].lower() + constChar
                
                curLine.insert( curIndices[0] + j + offset , curStr )   
                    
                offset += 1
                    
                curLine.insert( curIndices[0] + j + offset , curPart[-1])
                