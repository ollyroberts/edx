def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # TDD design
    tempStr = ''
    firstRun = True
    for x in secretWord:
    	if firstRun == False:
    		tempStr += ' '
    	else:
    		firstRun = False

    	if x in lettersGuessed:
    		tempStr += x
    	else:
    		tempStr += '_'

    return tempStr






#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))
#'_ p p _ e'