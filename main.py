import pygame
import textwrap
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
	return mystr_alphacoded
def chooseCard():
	template = int(input("Choose card type 1, 2, or 3: "))
	if template == 1:
		image = "assets/template_1.png"
		return image
	elif template == 2:
		image = "assets/template_2.png"
		return image
	elif template == 3:
		image = "assets/template_3.png"
		return image
	else:
		print("Invalid type, try running again")
def setScreen(image, text):
	screen = pygame.display.set_mode((1280, 720))
	background = pygame.Surface(screen.get_size())
	load_template = pygame.image.load(image)
	screen.blit(pygame.transform.scale(load_template, (1280, 720)), (0, 0))
	pygame.display.flip()
	pygame.font.init()
	font = pygame.font.SysFont('Comic Sans MS', 36)
	wrapped_text = textwrap.fill(text, 50)
	accum=0
	split_wrapped = wrapped_text.splitlines()
	for i in split_wrapped:	
		surface_text = font.render(i, True, (0, 0, 0))
		screen.blit(surface_text, (150, 100+(50 * accum)))
		pygame.display.update()
		accum += 1
	while True:
		pygame.event.pump()
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
def main():
	mystr = input("Please enter your string to be jumbled: ") 
	setScreen(chooseCard(), alphaCode(mystr))
main()