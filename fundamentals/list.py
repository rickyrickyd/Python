
fruit_list = ["apple", "banana", "cherry"]

def one():
    print(fruit_list)
    print(fruit_list[1])
    print(fruit_list[-1])
    print(fruit_list[0:2])

    print(len(fruit_list))

    if "apple" in fruit_list:
        print("Yes, 'apple' is in the fruit list")

    other_list =["apple", "banana", "cherry", 1, 10, "a", 5.3]

def two():
    fruit_list.append("orange")
    print(fruit_list)

    # Add fruit to fruit_list from middle by index
    fruit_list.insert(1, "Pear")
    print(fruit_list)

    # Modify item
    fruit_list[1] = "blackcurrant"
    print(fruit_list)

def three():
    # Remove specific item
    fruit_list.remove("banana")
    print(fruit_list)

    # Removes the specified index, or the last item if index is not specified
    fruit_list.pop(1)			# Remove fruit_list[1]
    fruit_list.pop()				#  Remove the last element

    fruit_list.clear()		# Empties the list

def four():
    # Iterate list by index
    for i in range(len(fruit_list)):
        print(fruit_list[i])

    # Iterate list by item
    for fruit in fruit_list:
        print(fruit)

def five():
    list_1 = ["a", "b", "c"]
    list_2 = [1, 2 ,3]

    list_3 = list_1 + list_2
    print(list_3)

    list_1.extend(list_2)
    print(list_1)

def six():
    fruit_tuple = ("apple", "banana", "cherry")
    print(fruit_tuple)
    print(fruit_tuple[1])
    print(fruit_tuple[-1])
    print(fruit_tuple[1:2])

    for fruit in fruit_tuple:
        print(fruit)
    
    if "apple" in fruit_tuple:
        print("Yes, 'apple' is in the fruit tuple")

two()