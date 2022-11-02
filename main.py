# importing random file.
import random
# importing art file.
import art

# importing os file for the clear function.
from os import system, name


def clear():
    # for windows.
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix').
    else:
        _ = system('clear')
# end of clear function.


# creating lists for all the letters upper and lower case, list for number and another for symbols.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '_', '-', '*', '+']


# main function.
def password_generator():
    # print the welcoming message and the app logo.
    clear()
    print(art.logo)
    print("Welcome to the Password Generator!")
    print("You need to enter how many letters, numbers, and symbols you need in your password.")
    print("-----------------------------------------------------")
    print()

    # asking the user to enter the number of letters, numbers, and symbols.
    number_of_letters = int(input("How many letters would you like in your password? "))
    number_of_numbers = int(input("How many numbers would you like? "))
    number_of_symbols = int(input("How many symbols would you like? "))

    password = ""
    characters = []

    # using for loops to loop number of times based on the user entry.
    # then push randomly from the letters, numbers, and symbols lists into the characters list.
    for letter in range(0, number_of_letters):
        characters.append(letters[random.randint(0, len(letters) - 1)])

    for number in range(0, number_of_numbers):
        characters.append(numbers[random.randint(0, len(numbers) - 1)])

    for symbol in range(0, number_of_symbols):
        characters.append(symbols[random.randint(0, len(symbols) - 1)])

    # shuffle the characters randomly before displaying it to the user.
    random.shuffle(characters)

    # adding the shuffled characters into the final password.
    for char in characters:
        password += char

    # printing the final result.
    print(f"Your password: {password}")


# end of main function.


# calling the function for the app to start.
password_generator()

is_continue = True
while is_continue:
    another_password = input("Do you want to generate another password Y or N? ").lower()
    if another_password == "y":
        clear()
        password_generator()
    elif another_password == "n":
        is_continue = False
        print("Thanks for using the app, GOODBYE.")
