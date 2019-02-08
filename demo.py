def codemaker(urstring):
	output=list(urstring)
	print(output)
	for index,letter in enumerate(urstring):
		for vowels in 'aeiou': 
			if letter==vowels:
				output[index]='x'
	return output
print(codemaker('Sammy'))