import random

# Simulation Parameters
starting_balance = 100
bet_amount = 10
flips = 50
current_balance = starting_balance

print("--- Starting Simulation ---")

# Simulate 50 coin flips one by one
for i in range(1, flips + 1):
    result = random.choice(["Heads", "Tails"])
    
    if result == "Heads":
        current_balance += bet_amount
    else:
        current_balance -= bet_amount
        
    print(f"Flip {i}: Result = {result} | Balance = ${current_balance}")
    
    if current_balance <= 0:
        print("❌ You went broke!")
        break

print(f"Final Balance: ${current_balance}")
