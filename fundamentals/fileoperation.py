file = open("file.txt", "w")
file.write("Now the file has more content!")
file.close()

with open("file.txt", "w") as w_file:
    w_file.write("Hello World!\n")
    w_file.write("Hellow World")


with open("file.txt", "r") as r_file:
    for line in r_file:
       print(w_file.readline(5))

