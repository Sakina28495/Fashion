seq={'john':10,'deric':20,'colt':30}
for char in seq:
	print(char)
	print("has a salary of: ")
	print(seq[char])
	print('')
for x in range(0,11,2):
	print(x)
print ('s'in'sdfghjkjhgtrertyrewrty')

def function(name="BLANK"):
	print ("reporting"+name)
function()

def add_num(num1,num2):
	return num1+num2 
result=add_num(2,4)
print(result)
mylist=['a','b','c']
for index,letter in enumerate(mylist):
	print(letter)
	print(f"is a index {index}")
	print('')