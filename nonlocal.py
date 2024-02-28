
def foo():
	name = "I am local" # Our local variable

	def bar():
		nonlocal name		 # Reference name in the upper scope
		name = 'I am non local' # Overwrite this variable
		print(name)
		
	# Calling inner function
	bar()
	
	# Printing local variable
	print(name)

foo()
