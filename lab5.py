# Lab 5 Azhar Saleh

# Cat function Step 1
def cat_greeting(word):
    print(f'cat says {word}')
    print('Cat says nothing')

cat_greeting("meow")

# Step 2
def generate_superhero_power():
    name = "Alex"
    power = "flying"
    print(f"{name} power is {power}")

generate_superhero_power()

# Step 3 
def generate_superhero_power():
    power = "flying"
    return power

print(generate_superhero_power())

# Step 4 
def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "1"
    return message 

print(generate_superhero_power2("mamica", "super human strength"))

# Step 5 
def cat_greetings_loop():
    for i in range(5):
        print(f'The cat says {greetings}')

    greetings = ["meow", "mo", "pur", "screech"]

    for i in greetings: 
        print("The cat says", i)

cat_greetings_loop()

# Step 6 Powers
def generate_multiple_powers(powers):
    for power in powers:
        print("Superhero Power:", power)

generate_multiple_powers(["Flying", "Invisibility", "Super Strength", "Time Travel"])