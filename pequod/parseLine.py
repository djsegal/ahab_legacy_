# -*- coding: utf-8 -*-
"""
Created on Sat May 31 14:38:48 2014

@author: dan
"""

from ahabSyntax   import commentChars

from splitRedLine import splitRedLine
from regroupConst import regroupConst

def parseLine( aLine ) :
    
    # ==================================
    #       ignore equal signs and
    #  allow commenting and blank lines 
    # ==================================

    aLine = aLine.replace( '=' , '' )

    aLine = aLine.strip()
    
    for aChar in commentChars :
        
        if aChar in aLine:
            
            aLine = aLine.split( aChar , 1 )[ 0 ]
                   
    if aLine == '' :
        
        return aLine
                    
    # =================================================
    #  split line and regroup the consts back together
    #        i.e. '@(' , 'a+' , 'b)' --> '@a+b@'       
    # =================================================

    curLine = splitRedLine( aLine )
    regroupConst( curLine )
    
    return curLine