def alphaCode(mystr):
	vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	mystr_alphacoded = ""
	for c in mystr:
		if c in vowels:
			number_vowels = ord(c)
			comp_number_vowels = number_vowels + 5
			mystr_alphacoded += chr(comp_number_vowels)
		elif c not in vowels:
			number_consonants = ord(c)
			if number_consonants < 65 or number_consonants > 122:
				mystr_alphacoded += chr(number_consonants)
			else:
				new_numbers = number_consonants - 21
				if new_numbers < 65:
					newer_numbers = new_numbers + 57
					mystr_alphacoded += str(newer_numbers)
				else:
					mystr_alphacoded += str(new_numbers)
	print(mystr_alphacoded)
def main():
	mystr = input("Please enter your string to be jumbled: ") 
	alphaCode(mystr)
main()