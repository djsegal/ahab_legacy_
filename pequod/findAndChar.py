# -*- coding: utf-8 -*-
"""
Created on Sat May 31 00:42:56 2014

@author: dan
"""

from ahabSyntax  import andChar

def findAndChar( curLine ) :
        
    # ======================================
    #  andChar has to be the very last char
    # ======================================
    
    if andChar not in curLine[ -1 ] :    
        
        return False
    
    # =================================
    #  now that we know 'and' has been
    #   found , remove it for curLine
    # =================================
    
    if len( curLine[-1] )  ==  2 and ']' in curLine[-1] :
        
        curLine[-1] = ']'
        
        return True    
    
    if len( curLine[-1] )   >  2  :
        
        curLine[-1] = curLine[-1][  0  :  len( curLine[-1] ) - 1  ]
        
        return True
        
    # ================================ 
    #  b/c it's not one of the above,
    #   curLine is just a '&' sign
    # ================================ 
        
    curLine.pop()     
        
    return True
    