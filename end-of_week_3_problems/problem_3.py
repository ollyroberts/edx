def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	yet been guessed in lowercase alphabetical order.
	'''
	import string
	alphaStr =string.ascii_lowercase
	tempStr = ''
	for x in alphaStr:
		if x in lettersGuessed:
			pass
		else: 
			tempStr += x

	return tempStr

lettersGuessed = []
print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz