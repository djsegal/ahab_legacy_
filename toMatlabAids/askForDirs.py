
from usedMsgs import inputRequest , inpErr1A , inpErr1B

def askForDirs( allData , curDirMsg ) :

    # ===========================
    #  ask user what directories
    #      they want scoured
    # ===========================

    done = False

    while not done :

        dirInput  =  raw_input( inputRequest )

        dirList   =  []

        # ----------------------------
        #  repeat dirMsg for the user
        # ----------------------------

        if not dirInput :

            print curDirMsg

            continue

        # --------------------
        #  parse user's input
        # --------------------

        strList  =  dirInput.split( ',' )

        strList  =  [ subParts for    part  in strList
                               for subParts in part.split() ]

        for aStr in strList :

            # ----------------------------------------
            #  allow colons, so have to test for them
            #      i.e.   1 : 3   -->   1 , 2 , 3
            # ----------------------------------------

            strSubList = aStr.split( ':' )

            # ------------------------------
            #  check for syntactical issues
            # ------------------------------

            if len( strSubList )  > 2 or not all( strSubList ) :

                break

            # ---------------------------------
            #  make sure they supplied numbers
            # ---------------------------------

            try :

                intVals = [ int(curNum) for curNum in strSubList ]

            except ValueError :

                break

            # -----------------------------
            #  expand out colon operations
            # -----------------------------

            if len( intVals ) == 2 :

                if intVals[1] > intVals[0] :

                    intVals = range( intVals[0] , intVals[1] + 1 )

                else:

                    intVals = reversed( range( intVals[1] , intVals[0] + 1 ) )

            # ------------------------------------
            #  make sure only the lists that were
            #  provided are selected by the user
            # ------------------------------------

            if max(intVals) > len(allData) :

                break

            # ------------------------
            #  if nothing went wrong,
            #  add the current values
            # ------------------------

            dirList.extend(  intVals  )

        else:

            done = True

        if not done :

            print inpErr1A + aStr + inpErr1B

    # ---------------------------------
    #    return the dir list after
    #  correct input has been supplied
    # ---------------------------------

    return dirList
