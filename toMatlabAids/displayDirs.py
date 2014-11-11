__author__ = 'dan'

from usedMsgs import preDirMsg

from math     import fmod

def displayDirs( allData ) :

    curDirMsg = preDirMsg + '     '

    for ( i , curFolder ) in enumerate( allData ) :

        # ------------------------------
        #    start index at 1 because
        #  humans are using this number
        # ------------------------------

        curInd = i + 1

        # --------------------------------
        #   prettify text for when there
        #  are less than 100 data folders
        # --------------------------------

        if curInd < 10 :

            curDirMsg  +=  '0' + str(curInd)

        else :

            curDirMsg  +=        str(curInd)

        curDirMsg  +=  ' : ' + curFolder + '      '

        # ------------------------
        #  for cosmetic purposes:
        #       add a space
        # ------------------------

        if len( curFolder ) < 12 :

            curDirMsg  +=  ' '

        # -------------------------------
        #  put two directories on a line
        # -------------------------------

        if int( fmod( curInd , 2 ) ) == 0 :

            curDirMsg  +=  '   \n'
            curDirMsg  +=  '     '

    return curDirMsg