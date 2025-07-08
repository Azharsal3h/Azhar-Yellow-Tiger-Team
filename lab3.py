food = "pizza with pepperoni"
print("First 3 letters:", food[:3])
print("Last 3 letters:", food[-3:])
new_string = food[0] + food[-1]
print("First and last letters combined:", new_string)
food_list = food.split()
print("Split into list:", food_list)
joined_food = " ".join(food_list)
print("Joined back to string:", joined_food)

number_list = [3, 6, 9, 12, 15]
number_list.append(18)
number_list.insert(3, 99)
number_list.pop()
number_list.remove(6)
print("Updated list:", number_list)
print("First 3 numbers:", number_list[:3])
print("Last 3 numbers:", number_list[-3:])

books = {
    "Rick Riordan": "Percy Jackson",
    "JK Rowling": "Harry Potter",
    "Suzanne Collins": "Hunger Games",
    "Dr. Seuss": "Green Eggs and Ham"
}
print("Authors:", list(books.keys()))
print("Books:", list(books.values()))
print("Book by JK Rowling:", books.get("JK Rowling"))
books.pop("Suzanne Collins")
print("After removing Suzanne Collins:", books)
del books["Rick Riordan"]
print("After deleting Rick Riordan:", books)


