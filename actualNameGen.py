import sys, random
print("\nWelcome to the greatest name generator on Earth.")
print("\n       Try not to be too intimidated")
first = ('peepee', 'poopoo', 'stinky', 'dumb', 'odd','weird', 'grimy', 'sploinky', 'scrumbobled', 'woinkled', 'Thom' )
last = ('bob', 'thomothy', 'grumble', 'scrimple', 'fellow', 'jimothy', 'weemy', 'garbage', 'ant', 'cell phone', 'Yorke')
# This has a small chance to output "Thom Yorke" from Radiohead. I did this because he should just go by Tom and is weird for throwing an "h" in there
while True:
	firstName = random.choice(first)
	lastName = random.choice(last)
	print("\n\n")
	print(firstName + " " + lastName)
# The book made this a lot more complicated, I just added the variables as strings
	try_again = input("\n\nTry again? (Press Enter, or Press n to quit)\n")
	if try_again.lower() == "n":
		break
input("\nPress Enter To Exit.")
# you still have to press any key to end it lmao