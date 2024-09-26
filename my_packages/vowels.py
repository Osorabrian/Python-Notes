from . import name
from . import vowel

def vowels(a,b):
	my_list = []
	name = name.full_name(a,b)
	for letter in name():
		if letter in vowel:
			my_list.append(letter)