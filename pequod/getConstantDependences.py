# -*- coding: utf-8 -*-

from ahabSyntax           import pythonMathWords , pythonMathChars , floatChars
from ahabErrorMessages    import err3      , err5

def getConstantDependences( inputValues , constsList ) :
    
    # -----------------------------
    #  values returned by function
    # -----------------------------
    
    bonusFloatStatus = False    # assume no new float information  
    constDependences = []
    
    # ---------------------------------------
    #  consts sorted by name (longest first)
    # ---------------------------------------
    
    sortedConsts = sorted( constsList , key=lambda curName : -len( curName ) )    
    
    # -------------------------------------------------------
    #  get the constant dependences for all the input values
    # -------------------------------------------------------
    
    for ( i , member ) in enumerate( inputValues ) :
                
        curDepend = []
        
        for inpVal in member:
                                
                # ------------------------------------
                #  get inpVal in a workable condition
                #     i.e., removing :  const chars  
                #                    &  white space
                # ------------------------------------
                
                newVal = ''.join( inpVal[1:-1].split() )
                
                # -------------------------------------------------------
                #  skip over inpVals that are only syntax (e.g. a comma)
                # -------------------------------------------------------
                
                if newVal == '' :
                    
                    continue
                
                # ----------------------------------
                #  require full sets of parentheses
                #   (   why not test it here ?  )
                # ----------------------------------
                
                if newVal.count('(') !=  newVal.count(')') :
                    
                    raise Exception( err3 )
                    
                # -----------------------------------------
                #  remove math chars and words from newVal
                # -----------------------------------------
                    
                for curChar in pythonMathChars + [')'] :
                    
                    if curChar in newVal :
                                
                        newVal = newVal.replace( curChar , '_' )
                        
                if len( newVal )  >  len( min( pythonMathWords , key = len ) ) + 1 :
                    
                    for curWord in pythonMathWords :
                        
                        if curWord in newVal :
                                
                            newVal = newVal.replace( curWord , '_' )
                                                
                # ========================================== 
                #  find all the constants used in this term
                # ==========================================
                    
                # ------------------------------------------
                #  for ease of the coder, this longPossName
                #    wont take into account removing math 
                #  syntax, even though it was removed first
                # ------------------------------------------
                 
                longPossName = len( newVal )
                
                for constName in sortedConsts :
                                    
                    # -------------------------------------------
                    #    short-circuit loop :
                    #      <>  when  all variables are found 
                    #      <>  for   vars with too long of names
                    # -------------------------------------------

                    if longPossName == 0 :
                        
                        break
                    
                    if len( constName ) > longPossName :
                        
                        continue
                    
                    # -----------------------------------------------
                    #  attempt to match const, 
                    #    if successful :  
                    #                    +  string replaced with '_'
                    #        [if needed] +  the dependence is added
                    # -----------------------------------------------

                    if constName in newVal :
                        
                        if constName not in curDepend :
                            
                            curDepend.append( constName )
                            
                        newVal = newVal.replace( constName , '_' )
                        
                        longPossName  =  len( 
                                         max( newVal.split('_') , 
                                                 key = len      ) )
                
                # ---------------------------------------------------
                #  at this point everthing is purged 
                #   === EXCEPT === numbers AND
                #                  float chars ( i.e. "." and "e" )
                #   THEREFORE , take this bonus chance to get floats
                # ---------------------------------------------------
                
                for curChar in floatChars :
                        
                    if curChar in newVal :
                        
                        # ---------------------------------  [|||]D
                        #  who doesn't love a bonus float?   
                        # ---------------------------------  [|||]D
                        
                        bonusFloatStatus = True   
                                                  
                        newVal = newVal.replace( curChar ,  '_' )


                # --------------------------------------------
                #  check for typos and unregistered variables
                # --------------------------------------------
                        
                if "(" in newVal :
                    
                    newVal = newVal.replace( "(" ,  '_' )
                          
                newVal = ''.join( newVal.split(     '_' )  )
                
                if newVal:
                    
                    # ----------------------------------
                    #  still present alphabetical chars  
                    #   will trigger an error here
                    # ----------------------------------
                    
                    try :
                        
                        int( newVal ) 
                        
                    except ValueError :
                        
                        raise Exception( err5 )
                            
        constDependences.append(curDepend)
            
    return ( bonusFloatStatus , constDependences )