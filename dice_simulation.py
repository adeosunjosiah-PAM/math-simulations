import random

# Roll a die 10,000 times randomly
rolls = [random.randint(1, 6) for _ in range(10000)]

# Count how many times the number 6 appeared
number_of_sixes = rolls.count(6)

print(f"The computer rolled the die 10,000 times.")
print(f"The number 6 appeared {number_of_sixes} times!")
