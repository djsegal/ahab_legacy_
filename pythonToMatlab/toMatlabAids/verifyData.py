__author__ = 'dan'

from usedMsgs   import continueMsg1A , continueMsg1B , continueMsg2 , inputRequest

from askForVars import askForVars

from verifyGo   import verifyGo

from math     import fmod

def verifyData( dirList , varList , allData ) :

    done        =  False    #  verification loop not done

    printBeg    =  True     #  print first  part of continue message
    printEnd    =  True     #  print second part of continue message

    curIncTry   =  0        #  the current number of incorrect tries is 0

    while not done :

        if printBeg :

            # -------------------------------------
            #  print beginning of continue message
            # -------------------------------------

            print continueMsg1A

            # ----------------------------
            #  print selected directories
            # ----------------------------

            curMsg   =  ' ' + 'curDirs' + ' :    '

            for ( j , curVar ) in enumerate( dirList ) :

                if j != 0  :

                    curMsg +=  ' ,  '

                    if int( fmod( j , 2 ) ) == 0 :

                        curMsg +=  '\n              '

                curMsg += str(curVar).ljust( 14 )

            print curMsg + '\n'

            # --------------------------
            #  print selected variables
            # --------------------------

            curMsg   =  ' ' + 'curVars' + ' :    '

            for ( j , curVar ) in enumerate( varList ) :

                if j != 0  :

                    curMsg +=  ' ,  '

                    if int( fmod( j , 2 ) ) == 0 :

                        curMsg +=  '\n              '

                curMsg += str(curVar).ljust( 14 )

            print curMsg + '\n'

            # -----------------------------------
            #  don't repeat this text every time
            #  the user types in something wrong
            # -----------------------------------

            printBeg = False

        # ---------------------------------------
        #  print second part of continue message
        # ---------------------------------------

        if printEnd :

            if curIncTry == 0 :

                print continueMsg1B

            else :

                print continueMsg2

        else :

            printEnd = True

        # ---------------------
        #  get input from user
        # ---------------------

        verifyInput  =  raw_input( inputRequest )

        verifyInput  =  verifyInput.strip()

        if not verifyInput :

            printEnd = False

            continue

        # ---------------------
        #  do desired protocol
        # ---------------------

        incorrectInput = False

        if   verifyInput[0] == 'y' :

            if verifyGo( dirList , varList ) :

                done = True

            else :

                # ------------------------------------
                #  this is equivalent to setting both
                #    printBeg and printEnd to False
                # ------------------------------------

                printEnd        =  False

                incorrectInput  =  True
                curIncTry   =  0

        elif verifyInput[0] == 'a' :

            print 'addDir'

        elif verifyInput[0] == 's' :

            print 'removeDir'

        elif verifyInput[0] == 'd' :

            askForVars( varList )

        elif verifyInput[0] == 'f' :

            print 'removeVar'

        else :

            incorrectInput = True

        # ------------------------------------------
        #  adjust the current incorrect try counter
        # ------------------------------------------

        if incorrectInput :

            curIncTry  +=  1

        else :

            curIncTry   =  0

        # ------------------------------------
        #   check if the first part of the
        #  continue message should be printed
        # ------------------------------------

        if fmod( curIncTry , 3 ) == 0 :

            printBeg = True

    # ---------------------------------------
    #  this function doesn't return anything
    #   it just manipulates data and checks
    #    when the user is ready to search
    # ---------------------------------------

    return