import requests
from requests.models import Response 

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)
print(response.content)

WORDS = response.text.splitlines()

print("   _____ \n"
        "  |     | \n"
        "  |     |\n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    / \ \n"
        "__|__\n")

with open("file.txt", "w") as w_file:
    
    for word in WORDS:
        w_file.write(word +'\n')