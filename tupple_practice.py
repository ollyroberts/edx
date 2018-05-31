tupple =('I', 'am', 'a', 'test', 'tuple')
def odd_tupples(atup):
	odd_tup =()
	counter = 0 
	for x in atup:
		if counter%2 == 1:
			odd_tup = odd_tup + (x,)
		counter = counter + 1 
	return odd_tup

print(odd_tupples(tupple))
