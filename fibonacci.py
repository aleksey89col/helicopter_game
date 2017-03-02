import __future__

class fibonacci :
	def __init__(self, num):

		self.fibonacci_list = []
		self.number = num
		self.index = 0

		# uses inner function to create the fibonacci series 
		self.create_fib(self.number)


		#print self.fibonacci_list
	
	def create_fib(self, num):
		# if num from init is 0 jsut return
		if num == 0:
			return

		# if the constructor passes a 1 return jsut 1 element 
		self.fibonacci_list.append(0)
		if num == 1:
			return
		
		#build the list that is bigger than 2
		self.fibonacci_list.append(1)
		
		for f in range(2, num):
			self.fibonacci_list.append(self.fibonacci_list[-1] + self.fibonacci_list[-2])


	def get_nums(self):
		return self.fibonacci_list

	#overload the str function
	def __str__(self) :
		return "The first {}  Fibonacci numbers are  {}".format(self.number, self.fibonacci_list)

	def __iter__(self) :
		return self

	def next(self) :
		if self.index >= len(self.fibonacci_list) :
			raise StopIteration

		return_val = self.fibonacci_list[self.index]
		self.index+=1

		return return_val

def fibonacci_gen(num = 0):
	current_list = fibonacci.get_nums()

	if current_list == 0 or current_list == 1 or num == 0:
		first, second = 0, 1

	else :
		first, second = current_list[-2], current_list[-1]


	while True :
		print "tupapa"
		yield first + second

		third = first + second
		first = copy.copy(second)
		second = copy.copy(third) 
		 


if __name__ == '__main__':
	x = fibonacci(100)

	print x

	x.get_nums()

	for i in range(0,5):
		print fibonacci_gen(), 














