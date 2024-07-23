import string
from time import sleep

print("Welcome to Palindrome Checker")


def checker(word):
    global original_word
    length = len(word)
    my_list = [0, 1]
    if length % 2 == 0 and length not in my_list:
        first_half = word[0:length // 2]
        second_half = (word[(length // 2):])[::-1]
        if first_half == second_half:
            print(f"{original_word} is palindrome")
        else:
            print("It's not a Palindrome")
    elif length % 2 == 1 and length not in my_list:
        first_half = word[0:(length // 2) + 1]
        second_half = word[(length // 2):][::-1]
        if first_half == second_half:
            print(f"{original_word} is palindrome")
        else:
            print("It's not a Palindrome")
    else:
        print("Enter a Valid input")

while True:
    print("Enter q to Quit.")
    user_word = input("Enter word to check: ").lower()

    if user_word == "q":
        break

    original_word = user_word.capitalize()

    ignore_list = [x for x in string.punctuation + "“" + "—"]

    for i in user_word:
        if i in ignore_list:
            user_word = user_word.replace(i, "")

    checker(user_word.replace(" ", ""))

print("Thanks for using!")
sleep(2)
