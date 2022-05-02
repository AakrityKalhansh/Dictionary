import json
import difflib

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(difflib.get_close_matches(word, data.keys()))>0:
        print("%s: " % difflib.get_close_matches(word, data.keys())[0])
        decide = input("pres y for yes or n for no: ")
        if decide == "y":
            return data[difflib.get_close_matches(word, data.keys())[0]]
        else:
            print("invalid word")
    else:
        print("invalid word")


word = input("Enter the word: ")
word = word.lower()
output = translate(word)
print(output)
