# -*- coding: utf-8 -*-
"""
Created on Tue May 27 02:23:37 2014

@author: dan
"""

from ahabSyntax         import openingChars    , closingChars  , incrementChars , constChar
from ahabSyntax         import pythonMetaChars , pythonEscChar

from ahabErrorMessages  import err4

from re                 import search          ,  split

def recursiveLineSeparate( line , curStartIndex ) :
    
    newLine = []    
    
    # ===========================================
    #  try to find constants named like @{_____}
    #          and separate them out
    # ===========================================
    
    for ( i , begChar ) in enumerate(  openingChars[ curStartIndex: ]  ) :
                
        if begChar in line :
            
            endChar = closingChars[i]
            
            if begChar in pythonMetaChars:
                
                begChar = pythonEscChar + begChar
                endChar = pythonEscChar + endChar
            
            curRegEx  = '('  + constChar + begChar 
            curRegEx += '[^' +  endChar  + ']*' 
            curRegEx +=         endChar  + ')'
            
            if search( curRegEx , line ) :
                
                newLine = filter( None     , [ item.strip() for item         
                        in split( curRegEx ,   line         )])
                                
                break 
                    
    else:
        
        # =============================================
        #  try to find a constant of the form "@_____"
        # =============================================
                
        # ---------------------------------------------       
        #  create bulk strings with all the char info
        #  ( also, dont want to remove parens inside )
        #  \      so remove ')' from bulkEnd        /
        # ---------------------------------------------
                
        bulkBeg   =  ''
        for begChar in openingChars :
            if begChar not in pythonMetaChars :
                bulkBeg += begChar
            else:
                bulkBeg += '\\' + begChar

        # ----------

        bulkEnd   =  ''
        tmpChars  =  closingChars[:]

        try :
            tmpChars.remove( ')' )
        except ValueError :
            print err4
            
        for endChar in tmpChars + incrementChars :
            if endChar not in pythonMetaChars :
                bulkEnd += endChar
            else:
                bulkEnd += '\\' + endChar
                         
        # ----------------------------------------------
        #  create the needed regular expression formula
        # ----------------------------------------------
               
        curRegEx  =  '(' + constChar + '[^' + bulkBeg +        ']'
        curRegEx +=                    '[^' + bulkEnd + '\s' + ']' + '*)'
                      
        # -----------------------------------------------              
        #  if a constant is found the last way possible,
        #    return those values upwards (recursively)
        # -----------------------------------------------
                      
        if search( curRegEx , line ) :
            
            newLine = filter(  None     , [ item.strip() for item         
                    in split(  curRegEx ,   line                   )])     
                    
            return newLine

    # --------------------------
    #   if it's not a new line,
    #  just return a list of it
    # --------------------------

    if not newLine :
        
        return [ line ]
        
    # ------------------------------------
    #     create the returned list by 
    #   recursively calling this function
    # ------------------------------------
               
    returnedLine = []
    
    for part in newLine :

        returnedLine += recursiveLineSeparate( part , i+1 )
        if not returnedLine[-1] :
            returnedLine.pop()
                            
    return returnedLine
    
