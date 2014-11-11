__author__ = 'dan'

from usedMsgs import verifyGoErr

def verifyGo( dirList , varList ) :

    # =============================================
    #         really an unneeded function.
    #  it tests completeness just to thwart people
    #    who remove all the dirs and all the vars
    #     after the initial ones have been added
    # =============================================

    if dirList :

        if varList :

            return True

        else :

            curStr  =  '          You need to add Variables.            '

    else :

        if varList :

            curStr  =  '         You need to add Directories.           '

        else :

            curStr  =  ' You need to add BOTH Directories and Variables.'


    print verifyGoErr + curStr + verifyGoErr

    return False