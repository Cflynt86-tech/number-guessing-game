# This code is made by CFlynt86_tech
import random
import math

print("Hello, this number guessing game is one i hope you will enjoy" \")
lower, upper, max_a = 1, 50, 7
secret= random.randint(lower, upper)
while attempts< max_a:
try:
guess= int(input(f"Attemmpt{attempts+1}:"))
if not (lower<=guess<= upper):
print(f"Out of range!"); continue
attempts += 1
if guess == secret:
print(f"Correct! Took {attempts}tries."); return
print("Too low!"if guess< secretelse"Too high!")
except ValueError:
print("Invaledinput! Enter an integer.")
print(f"Game over! The number was {secret}.")

play_game()
