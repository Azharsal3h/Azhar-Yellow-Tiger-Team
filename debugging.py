# debugging  Azhar Saleh
# code snippet 1 
# ZeroDivisionError we changed the number to 2 instead of 0
print("Code Snippet 1")
x = 10
y = 4 
result = x / y
print("Result:", result)

# Snippet 2 
#indexerrorwrong; "i +1 " we removed +1
# Incorrect:
print("Code Snippet 2")
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

#snippet 3
#syntaxerror missing :
print("Code Snippet 3")
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

# snippet 4
# Incorrect: missing :
print("Code Snippet 4")
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# snippet 5
#missing :
for i in range(5):
   print(i)

# snippet 6 
#the "," was in the wrong place
# Incorrect:
def greet(name):
   return "Hello", + name
 
print(greet("Alice"))

#snippet 7 
# i had to put a indent infront of sum
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

# snippet 8 
# nothing came out wrong with this?
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n+1)

#snippet 9 
# fixed it i put "name =="
name = input("Enter your name: ")
if name == "stranger" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger")

# snippet 10 
# 
def divide_numbers(x, y):
   if y == 0:
      return "Error: Cannot divide by zero"
   result = x / y
   return result
 
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))
