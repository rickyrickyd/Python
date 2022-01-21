import requests
from random import randint
from requests.models import Response, guess_filename 
from os import system

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)
WORDS = response.text.splitlines()
random_index = randint(0, len(WORDS) -1 )


def output_word():
    for chr in user_word:
        print(chr, end=" ")

def output_hangman(wrong):
    if (wrong == 0):
        print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |       \n"
        "  |        \n"
        "  |        \n"
        "__|__")
    if (wrong == 1):
        print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |     O \n"
        "  |        \n"
        "  |        \n"
        "__|__")
    if (wrong == 2):
        print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |     O \n"
        "  |     |   \n"
        "  |        \n"
        "__|__")
    if (wrong == 3):
        print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|   \n"
        "  |        \n"
        "__|__")
    if (wrong == 4):
        print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\  \n"
        "  |        \n"
        "__|__")
    if (wrong == 5):
        print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\  \n"
        "  |    /   \n"
        "__|__")
    if (wrong == 6):
                print("   _____ \n"
        "  |     | \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\  \n"
        "  |    / \   \n"
        "__|__")
word_list = []

with open("file.txt", "r") as r_file:
    word_list = r_file.readlines()

word = word_list[randint(0, len(word_list)-1)]

guess_answer = []

user_word = []
wrong = 0
word = word.strip()

with open("file.txt", "w") as w_file:
    for word in WORDS:
        w_file.write(word +'\n')
 
min_length = 4  

while (len(word) <= min_length):
    random_index = randint(0, len(WORDS) -1 )
    word = WORDS[random_index]

for i in range(len(word)):
    user_word.append("_")
    print(len(user_word[i]))

for i in range(20):
    if "_" in user_word:
        if (wrong <= 5):
            system("cls")
            print("Let's play Hangman")
            print("total of letters:", len(word))
            print(guess_answer)
            output_hangman(wrong)
            output_word()
            answer = input('\n\nType letter:')
            guess_answer.insert(1, answer)
            
            not_match = False
            for i in range(len(word)):
                if(answer == word[i]):
                    user_word[i] = answer
                    not_match = True
            if not not_match:
                wrong += 1
        else:
            system("cls")
            output_hangman(wrong)
            output_word()
            print("\n You lost!")
            print("The word is", word)
            exit()
    else:
        print()
        output_word()
        print("\nYou won!")

if (wrong >= 5):
    system("cls")
    output_word()
    print("\nYou lose!")
    print("The word is", word)
