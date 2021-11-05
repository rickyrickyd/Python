var = input()
my_int = int(input("Enter integer: "))
print(my_int)
my_int = float(input("Enter integer: "))
print(my_int)
import sys
line = sys.stdin.readline
for line in sys.stdin:
    print(line)
all_data = sys.stdin.read().split('\n')

var = input()

print(type(var))

print(type(str))