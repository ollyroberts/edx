animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(exDict):
	tempDict = {}
	for key in exDict:
		tempDict[key] =(len(exDict[key]))
	return max(tempDict,key=tempDict.get)
print(biggest(animals))

def animalCount(x):
	counter = 0
	animalList =[]
	for animal in x.values():
		for x in animal:
			counter += 1
	return(counter)
 

