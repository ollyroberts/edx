def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # LETS TRY SOME TDD
    #I) uniLetter us a [] of unique letters in secret word 
    #II) if every letter in uniLetter is in lettersGuessed Return True 

    #I)
    uniLetter = []
    for x in secretWord:
        if x in uniLetter:
            pass
        else:
            uniLetter.append(x)

    #uniLetter = ['a', 'p', 'l', 'e']

    #II)
    guessed = True


    for x in uniLetter:
        if x in lettersGuessed:
            guessed == True
        else:
             guessed = False
             return guessed
    return guessed 

#secretWord = 'bat' 
#lettersGuessed = []
#print(isWordGuessed(secretWord, lettersGuessed))


