def empty_function():
    pass

def my_function():
    print("Hello from a function")

empty_function()
my_function()

def my_function(first_str, second_str):
    print(first_str + " " + second_str)

my_function("Ottawa STEM", "Club")


def my_function(child_1, child_2, child_3="Lisa"):
    print("The third child is " + child_3)

my_function(child_1="Alvin", child_2="Bruce")
my_function(child_1="Alvin", child_2="Bruce", child_3="Carol")


def my_function(x):
    return 5 * x

y = my_function(x=3)
print(y)

print(my_function(x=5))