# -*- coding: utf-8 -*-
"""
Created on Fri May 30 21:06:23 2014

@author: dan
"""

from recursiveLineSeparate  import  recursiveLineSeparate
from ahabSyntax             import  constChar

def splitRedLine( aLine ) :

    # ==========================================
    #  use standard split in two cases, when :
    #       (1) curVar being read is a const.
    #           consts can't depend on other
    #           consts, so they're splittable
    #       (2) there is no const in the line
    # ==========================================

    if  aLine[0] == constChar or constChar not in aLine :
        
        curLine  =  aLine.split()
        return curLine
        
    # ================================================================
    #  separate the const terms from the other vector terms.
    #   +  when all else fails, use regular expressions      - G-D
    #   +  yeah, i know. this isnt the most elegant way      - Dingus
    # ================================================================

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  first , separate line according to ahabSyntax
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    curLine  =  recursiveLineSeparate( aLine , 0 )
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  second, split line like in the if part above          
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    offSet   =  0
    
    for j in range( len( curLine ) ) :

        # =================================
        #       skip over consts b/c 
        #  they can't be touching anything
        # =================================
        
        if curLine[ j + offSet ][ 0 ] == constChar :
            
            continue
        
        # -------------------------------------------------
        #  split the current part of red.inp into subparts
        # -------------------------------------------------
        
        tmpParts = curLine[ j + offSet ].split()

        # ==============================
        #  if there's only one subpart,
        #    skip the separation step 
        # ==============================
        
        if len( tmpParts ) <= 1 :
            
            continue

        # -------------------------------------                                
        #  pop off part that is being replaced
        # -------------------------------------
                                
        curLine.pop( j + offSet )
        
        offSet -= 1

        # ============================      
        #    replace popped off part
        #  with the corrected version
        # ============================
        
        for aPart in tmpParts :
            
            offSet += 1
            
            curLine.insert( j + offSet , aPart )
    
    return curLine
                    