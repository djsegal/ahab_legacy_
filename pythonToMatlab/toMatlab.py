
from  os                         import  getcwd , walk

from  toMatlabAids.usedMsgs      import  introMsg , dirMsg , varMsg

from  toMatlabAids.displayDirs   import  displayDirs

from  toMatlabAids.askForDirs    import  askForDirs

from  toMatlabAids.askForVars    import  askForVars

from  toMatlabAids.verifyData    import  verifyData

from numpy import array , concatenate

import numpy as np

from scipy.io   import savemat

# =============================
#  function for allowing users
#   to parse their data files
# =============================

origDir  =  getcwd()

dataDir  =  origDir  +  '/data/'

# =============================
#  get list of dirs to inspect
# =============================

allData  =  walk(dataDir).next()[1]

strLen   =  len( max( allData , key=len ) )

allData  =  [ curStr.ljust( strLen ) for curStr in allData ]

# ========================
#   display intro message
#   and the list of dirs
# ========================

print introMsg

curDirMsg  =  displayDirs( allData )

print curDirMsg

# ======================
#   ask user to select:
#    +  dirs to scour
#    +  vars to hunt
# ======================

print dirMsg

dirList  =  askForDirs( allData , curDirMsg )

print varMsg

varList  =  askForVars( [] )

# ==============================
#   verify data with user and
#  ask them if they want to run
# ==============================

verifyData( dirList , varList , allData )

# ===========
#  seek data
# ===========

aRepeatedWord  =  ''

for curDir in dirList :

    # -----------------------------------------------
    #  have to subtract one because the indices were
    #     offset for easier reading comprehension
    # -----------------------------------------------

    relPathForCurDir = dataDir + allData[ curDir - 1 ] + '/'

    # -----------------------------------------------
    #  get list of sub-dirs to inspect.   equivalent
    #    to initial directory read in toMatlab
    # -----------------------------------------------

    allSubDirs  =  walk( relPathForCurDir ).next()[ 1 ]

    for curSubDir in allSubDirs :

        # -----------------------------------
        #  open cur sub-dir's bucky.out file
        #      and read it line-by-line
        # -----------------------------------

        curFileName       =  relPathForCurDir + curSubDir + '/bucky.out'

        curInput          =  open(  curFileName , 'r'  )

        curMatchedVar     =  ''

        stillMatched      =  False

        immediateNewVar   =  False

        curVarArrayList   =  [ [] ] * len( varList )

        curVarList        =  []

        for curLine in curInput :

            # -----------------------------------------------
            #  remove excess leading and trailing whitespace
            #   from the line and continue if it's empty
            # -----------------------------------------------

            curLine = curLine.strip()

            if not curLine :

                continue

            # ---------------------------------
            #    look at the first element of
            #  curLine to determine what to do
            # ---------------------------------

            if not curMatchedVar and ( curLine[0].isdigit() or curLine[0] == '-' ):

                continue

            if curMatchedVar and not curLine[0].isdigit() and not curLine[0] == '-' :

                # ======================================
                #        three possible outcomes
                # ======================================
                #  (1) another sought variable is next
                #  (2) the variable is finished
                #  (3) there is a line of text after
                #      the var that needs to be ignored
                # ======================================

                # -------------------------------------
                #  (1) another sought variable is next
                # -------------------------------------

                for ( curInd , curVar )  in  enumerate( varList )  :

                    if curVar == sepCurLine[0] :

                        break

                if curMatchedVar   != curVar :

                    immediateNewVar = True

                    aRepeatedWord   = ''

                # --------------------------------------
                #  (2) the variable is finished  -OR-
                #  (3) there is a line of text after
                #      the var that needs to be ignored
                # --------------------------------------

                if curVarList and curLine[0] != aRepeatedWord :

                    stillMatched   =  False

                    aRepeatedWord  =  ''

                else :

                    aRepeatedWord = curLine[0]

                    continue

            # ------------------------------------------------
            #   if the current variable is no longer matched
            #  add its current list to its encompassing array
            # ------------------------------------------------

            if curMatchedVar and not stillMatched :

                # --------------------------------------------
                #        how curVarArrayList is made.
                #  if statements in order of creation process
                # --------------------------------------------

                if not np.any( curVarArrayList[ curInd ] ) :

                    curVarArrayList[ curInd ]  =  curVarList

                elif isinstance( curVarArrayList[ curInd ] , list ) :

                    curVarArrayList[ curInd ]  =  array( [
                        curVarArrayList[ curInd ]  ,  curVarList   ] )

                else :

                    curVarArrayList[ curInd ]  =  concatenate(
                        curVarArrayList[ curInd ]  ,  array(curVarList)   )

                curMatchedVar  =  ''
                curVarList     =  []

                if not immediateNewVar :

                    continue

                else :

                    immediateNewVar = False

            # ---------------------------------------------
            #  split line to get ready for the next step :
            #    either adding data  OR  hunting for vars
            # ---------------------------------------------

            sepCurLine = curLine.split()

            # ----------------------------
            #  read in requested data and
            # ----------------------------

            if curMatchedVar :

                try :

                    curVarList.extend(  [ int(curNum) for curNum in sepCurLine ]  )

                except ValueError:

                    try :

                        curVarList.extend(  [ float(curNum) for curNum in sepCurLine ]  )

                    except ValueError :
                        print sepCurLine
                        replaceThisMessage  = 'fix this later by telling people: '
                        replaceThisMessage += 'the dir name, the var name, the line number, etc.'
                        raise Exception( replaceThisMessage )

                continue

            # --------------------------------------
            #  try to match a sought after variable
            # --------------------------------------

            for ( curInd , curVar )  in  enumerate( varList )  :

                if curVar == sepCurLine[0] :

                    curMatchedVar  =  curVar

                    stillMatched   =  True

                    break

        # -------------------------------------------
        #  if there is only one cycle in an output ,
        #    make sure you turn it into an array
        # -------------------------------------------

        if isinstance( curVarArrayList[ 0 ] , list ) :
            print 123
            for k in range(  len( curVarArrayList )  )  :

                curVarArrayList[ k ]  =  array( [  curVarArrayList[ k ]  ] )

        curInput.close()

        for ( curInd , curArray ) in enumerate( curVarArrayList ) :

            newFileName   =  relPathForCurDir

            newFileName  +=  varList[curInd] + '_' + curSubDir + '.mat'

            savemat( newFileName , mdict={'arr': curArray} )

    # -----------------------------------------
    #  if there is only one subdir in an dir ,
    #    make sure you turn it into an array
    # -----------------------------------------

    if curMatchedVar and not stillMatched and isinstance( curVarArrayList[ 0 ] , list ) :

        print 321
        for k in range(  len( curVarArrayList )  )  :

            curVarArrayList[ k ]  =  array( [  curVarArrayList[ k ]  ] )


print ' ok done '