###############################################################################
# Introduction
###############################################################################

# The purpose of this script is to autogenerate a secure password for the user.
# Each password will be 15 characters in length and include a minimum of one or
# more characters from each of the following character types:
# - lower case letters
# - upper case letters
# - numbers
# - symbols

###############################################################################
# Import Libraries
###############################################################################

import random

###############################################################################
# Create Variables
###############################################################################

# create a variable containing all lower case characters
lower_case = "abcdefghijklmnopqrstuvwxyz"

# create a variable containing all upper case characters
upper_case = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"

# create a variable containing all numeric characters
numbers = "0123456789"

# create a variable containing all symbol characters
symbols = "!@#$%^&*?"

# create a variable containging the length of the password
password_length = 15

# randomly generate the count of numbers and symbols for the password
# a minimum of one character and a maximum of three characters
# will be selected for each character type
number_count = random.randint(1, 3)
symbol_count = random.randint(1, 3)

# using the randomized character count, the number/s and symbol/s will not be
# randomly selected from the corresponding list of characters
selected_numbers = "".join(random.sample(numbers, number_count))
selected_symbols = "".join(random.sample(symbols, symbol_count))

# count the number of selected characters of both numbers and symbols
selected_number_length = len(selected_numbers)
selected_symbols_length = len(selected_symbols)

# the count of characters is subtracted from 15 to calculate the remaining
# count of characters needed for the password
remaining_length = 15 - (selected_symbols_length + selected_number_length)

# the lower case count is determined randomly, leaving at least one character
# for upper case characters
lower_case_count = random.randint(1, (remaining_length-1))

# the upper case count is calculated
upper_case_count = remaining_length - lower_case_count

# the lower and uppercase characters are randomly selected
selected_lower_case = "".join(random.sample(lower_case, lower_case_count))
selected_upper_case = "".join(random.sample(upper_case, upper_case_count))

# all randomly selected characters are added into one string
password_string = str(selected_numbers) + selected_symbols + \
    selected_lower_case + selected_upper_case

# the selected characters are placed into a list to support random order
characters = list(password_string)

# the list of selected characters are suffled
random.shuffle(characters)

# the suffled character list is then put into a string
generated_password = "".join(characters)

# the string is printed as the user's new password
print(f'Your auto-generated password is: {generated_password}')