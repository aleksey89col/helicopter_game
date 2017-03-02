#!/usr/bin/env python
# Helmut Cardenas fsuid:hac14d
import sys
import string
import time


def log(file_name = None) :
	def log_decorator(func) :
		def new_func(*args) :
			file_bool = False
			# if file is passed redirect stdout to a file
			if file_name != None :
				try:
					file = open(file_name, 'a')
					sys.stdout = file
					file_bool = True
				except Exception as e:
					sys.stdout = sys.__stdout__


			print("*************************************************")
			print ("Calling function " + func.__name__)

			# check for arguments 
			if len(args) == 0 :
				print("No arguments")
			else :
				for arg in args :
					print("\t- " + str(arg) + " of type " + str(type(arg).__name__) + ".")


			
			print("Output:")

			# we get the start time in order to measure how long it took
			# and i also use return value to print it to screen
			time_start = time.time()
			return_val = func(*args)
			time_end = time.time() - time_start 
			print ("Execution time: %.5f s. " %  round(time_end, 5) )
			

			if return_val == None :
				print("No return value.")
			else:
				print ("Return value: " , return_val)


			print("*************************************************\n")
			# closes file redirects stdout from file to stdout
			if file_bool :
				file.close()
				sys.stdout = sys.__stdout__

		return new_func
	return log_decorator


@log()
def factorial(*num_list):
	results = []
	for number in num_list:
		res = number
		for i in range(number-1,0,-1):
			res = i*res
		results.append(res)
	return results


@log("logger.txt")
def waste_time(a, b, c):
	print("Wasting time.")
	time.sleep(5)
	return a, b, c


@log("logger.txt")
def gcd(a, b):
	print("The GCD of", a, "and", b, "is ", end="")
	while a!=b:
		if a > b:
			a -= b
		else:
			b -= a
	print(abs(a))
	return abs(a)


@log()
def print_hello():
	print("Hello!")


@log(10)
def print_goodbye():
	print("Goodbye!")


if __name__ == "__main__":
	factorial(4, 5)
	waste_time("one", 2, "3")
	gcd(15,9)
	print_hello()
	print_goodbye()