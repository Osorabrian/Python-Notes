# n = 6
# i = 0

# while i < n:
# 	while i < n:
# 		print(n * "*")
# 		i += 1
# 	i += 1



# def sqaure_of_stars_with_for(user_input):
#     for i in range(user_input):
#         print(user_input * "*")

# sqaure_of_stars_with_for(8)

# def lower_triangle_with_while(n):

# 	i = 1
# 	while i <= n:
# 	 	print(i * "*")
# 	 	i += 1

# lower_triangle_with_while(5)

# def lower_triangle_with_for():
# 	for i in range(5):
# 		print(i * "*")

# lower_triangle_with_for()

# def upper_triangle_with_while(n):

# 	for i in range(n, 0, -1):
# 		print(i * "*")


# def isosceles_triangle(n):
# 	lower_triangle_with_while(n-1)
# 	upper_triangle_with_while(n)

# isosceles_triangle(10)

# def is_prime(number):


# 	for i in range(2, number):
# 		if number % i == 0:
# 			print(i)

	

# is_prime(8)

# my_list = []
# def prime_factors(n):
# 	for i in range(2, n):
# 		if n % i == 0:
# 			if is_prime(i) == True:
# 				my_list.append(i)

# prime_factors(50)
# print(set(my_list))

# def trees_and_five():

# 	for i in range(50):
# 		if i % 3 == 0 and i % 5 == 0:
# 			print("Trees and Fives")
# 		elif i % 5 == 0:
# 			print("Fives")
# 		elif i % 3 == 0 :
# 			print("Trees")
# 		else:
# 			print(i)

# trees_and_five()

# def concat_sentence(sentence):

# 	s_list = sentence.split()
# 	new_name = ""

# 	for index, name in enumerate(s_list):
# 		if index < len(s_list)-1:
# 			for index, letter in enumerate(name):
# 				if index < len(name)-1:
# 					new_name += letter + "-"
# 				else:
# 					new_name += letter + "__"
# 		else:
# 			for index, letter in enumerate(name):
# 				if index < len(name)-1:
# 					new_name += letter+"-"
# 				else:
# 					new_name += letter

# 	return new_name

# print(concat_sentence("my name is Brian"))


def prime_numbers():

	for i in range(2, 10):
		for n in range(2, i):
			if i % n == 0:
				break
			else:
				print(i)

def is_prime(n):

	prime = True

	for num in range(2, n):
		if n % num == 0:
			prime = False

	return prime

def prime_factors(n):
	
	prime_list = []
	for i in range(n):
		for x in range(n):
			if i * x == n:
				if is_prime(i):
					prime_list.append(i)
	return prime_list

print(prime_factors(50))
