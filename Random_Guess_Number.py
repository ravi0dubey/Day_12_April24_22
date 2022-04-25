import random
from art import logo

print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1,100)
print(f"number_to_guess: {number_to_guess}")
level = input("Choose a  difficulty. Type 'easy' or 'hard':")

     
if level == 'easy':
  no_of_attempts = 10
else:
  no_of_attempts = 5

while no_of_attempts != 0:
  print(f"You have {no_of_attempts} attempts remaining to guess the number")
  your_guess = int(input("Make a guess: "))
  no_of_attempts -= 1
  if your_guess > number_to_guess:
    print("Too High")
  elif your_guess < number_to_guess:
    print("Too Low")
  else:
    print("You guessed it correctly")
    break
  if(no_of_attempts ==0 and your_guess !=number_to_guess):
    print("You've run out of guesses, you lose")
  else:
    print("Guess Again")
  



   