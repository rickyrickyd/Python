# pip install requests
import requests         # Web Scraper
from random import randint
from os import system

# url = 'https://www.mit.edu/~ecprice/wordlist.10000'
# response = requests.get(url)
# WORDS = response.text.splitlines()              # WORDS is List,  ASCII '\n', 10000
# # print(WORDS)
# # my_text = "a\nb\nc\n"
# # print(my_text.splitlines())

# # random_index = randint(0, len(WORDS)-1)         # Range
# # print(WORDS[random_index])

# with open("words.txt", "w") as w_file:
#     for word in WORDS:
#         w_file.write(word + '\n')
#     # w_file.write(str(response.text.splitlines()))         # Write list (JSON) to file 

user_word = []
wrong = 0

def output_hangman(wrong):
    if (wrong == 0):
        pass
    if (wrong == 1): 
        print("   _____ \n"
            "  |     | \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n")
    if (wrong == 2): 
        print("   _____ \n"
            "  |     | \n"
            "  |     | \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n")
    if (wrong == 3): 
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     \n"
            "  |     \n"
            "  |     \n"
            "__|__\n")
    if (wrong == 4): 
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n")

def output_word():
    for chr in user_word:
        print(chr, end=" ")

word_list = []
with open("file.txt", "r") as r_file:
    word_list = r_file.readlines()          # Option 1
    # word_list = r_file.read().splitlines()  # Option 2

word = word_list[randint(0, len(word_list)-1)]
min_length = 5
while (len(word) < min_length):
    word = word_list[randint(0, len(word_list)-1)]

system("cls")
word = word.strip()

# Prepare number of underscore
for i in range(len(word)):
    user_word.append("_")

# Only keep 4 letter for input
while (user_word.count("_") > 4):
    prepare_chr = chr(96 + randint(1, 26))
    for i in range(len(word)):
        if (prepare_chr == word[i]):
            user_word[i] = prepare_chr

for i in range(4):
    if "_" in user_word:
        if (wrong < 4):
            system("cls")
            print("Let's play Hangman game!")
            print("This word has total {} letters.".format(len(word)))
            print(word)
            output_hangman(wrong)   # Use the wrong for output hangman
            output_word()
            chr_input = input("\n\nInput the char: ")
            not_match = False
            for i in range(len(word)):
                if (chr_input == word[i]):
                    user_word[i] = chr_input
                    not_match = True
            if not not_match:
                wrong += 1
        else:
            # Handel the lost
            system("cls")
            output_hangman(wrong)
            output_word()
            print("\n You lost!")
            print("The word is", word)
            exit()
    else:
        # Handle the win
        print()
        output_word()
        print("\nYou won!")

if (wrong < 5):
    # Handle the win
    system("cls")
    output_word()
    print("\n You Win!")
else:
    # Handle the Lost
    system("cls")
    output_hangman(wrong)
    print("\n You lost!")
    print("The word is", word)


