import random

mystery = random.randint(1, 100)
score = 0

while True:
	guess = int(input("guess a number from 1 to 100, mk? "))
	score += 1 # guess = guess +1
	if guess == mystery:
		print("wow !! u didnt suck :)")
		break
	elif guess > mystery:
		print("aim lower, just like my life")
	else:
		print("get highhhhhh")

print("you did your best and guessed "+ str(score)+" times")