# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:17:00 2013

@author: dan
"""

from shutil         import copyfile
from os             import makedirs

def makeBuckyInputs( curDir , varList , valueCombinations ):

    # --------------------------------
    #  find the location in bucky.inp
    #    where info should be added
    # --------------------------------

    buckyInput  =  open(  'bucky.inp'  ,  'r'  )
    done        =  False
    offset      =  0
    
    while ( not done ):
        
        buckyInput.seek(offset,2)
        line = buckyInput.read()
        
        if '$' in line:
            
            done   = True
            
        offset = offset - 1
        
    buckyInput.close()    

    # ----------------------------- 
    #  loop over all possible jobs
    # -----------------------------    

    strLen  =  len( valueCombinations )
    strLen  =  len(   str( strLen )   )
    
    for ( i , curCombo ) in enumerate( valueCombinations ) :  

        # ----------------------------------------
        #  make directory and put bucky.inp there
        # ----------------------------------------

        newDir     =  curDir  +  '/'  +  str( i ).zfill( strLen )
        
        makedirs(     newDir  )
        
        curFile    =  newDir  +  '/'  +  'bucky.inp'  
        
        copyfile( 'bucky.inp' , curFile )
        
        # ------------------------------------------
        #  modify the current directory's bucky.inp 
        # ------------------------------------------
        
        tmpInput = open(curFile, 'r+')
        tmpInput.seek(offset,2)
        
        tmpInput.write( '\n!   -------------------------------------       ' )
        tmpInput.write( '\n!    variables added for parameter sweep        ' )
        tmpInput.write( '\n!   -------------------------------------   \n\n' )
        
        for ( j , curVar ) in enumerate( varList ) :

            # -------------------------------
            #  get the string representation 
            #    for the current variable
            # -------------------------------
      
            if type(curCombo[j]) != list :
                
                curItem  =  str( curCombo[j] )    
                
            else :
                
                curItem  =  ' , \n \t\t\t '
                
                curItem  =  curItem.join(  str(  num  ) 
                                           for   num  in  curCombo[j]  )              

            # -------------------------------                        
            #    print current variables's 
            #  string representation to file
            # -------------------------------
                        
            curString   =  '     '  +  curVar
            curString  +=   ' = '   +  curItem  +  ' \n'       
            
            tmpInput.write( curString )
    
        # ----------------------------------------
        #  wrap up current directory's input file
        # ----------------------------------------    
    
        tmpInput.write( '\n $end \n' )
        
    tmpInput.close()