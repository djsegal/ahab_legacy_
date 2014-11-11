
from usedMsgs import inputRequest , varMsg

from math     import fmod

def removeVars( varList ) :

    # ======================
    #  remove unwanted vars
    # ======================

    done           =  False

    varAddCounter  =  0

    while not done :

        if varList :

            varAddCounter += 1

            curMsg  =  '  curVars   :  '

            for ( i , curVar ) in enumerate( varList ) :

                if i != 0  :

                    curMsg +=  ' ,  '

                    if int( fmod( i , 2 ) ) == 0 :

                        curMsg +=  '  \n               '

                curMsg += curVar.ljust( 14 )

            if int( fmod( varAddCounter , 5 ) ) == 0 :

                print varMsg

            print curMsg + '\n'

        varInput  =  raw_input( inputRequest )

        print ''

        # -------------------------------------
        #  check if varList has been completed
        # -------------------------------------

        if not varInput :

            if varList :

                done = True

            else :

                print '\n You need to insert at least one variable to hunt. \n'
                continue

        varInput =  varInput.replace( ',' , '' )

        varList.extend(  varInput.split()  )

    return varList
