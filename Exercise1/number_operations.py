# Directions:
# Clone repo from https://github.com/tapizquent/python_course.git

# - Add the missing part so the programs compiles and runs
# - When the program runs, before anything else, prompt the user with the following
#   message: 'What is your name? '
# And then write to the screen: 'Hello, FIRST_NAME LAST_NAME. Welcome to addition!'
#
# - The user should be able to input 2 numbers (this is fine if it's done in two lines)
# - Then print to the screen: the sum, multiplication, subtraction and exponent (a^b) of these 2 numbers
#   that is, if user inputs 1 and 2,
#   the output should be
#   => SUM: 3
#      SUB: -1
#      MULT: 2
#      EXP: 1

# Ask user for their first and last name here

first_name = input('Input your first name: ')
last_name = input('Input you last name: ')

print()
print(f'Hello, {first_name} {last_name} Welcome to addition!')
print()

# Ask user to input first number
a = int(input("Enter your frist number: "))
# Ask user to input second number
b = int(input("Enter you second number: "))

sum = a+b
subt = a-b
mult = a*b
exp = a**b

print()
print(f'SUM: {sum}')
print(f'SUB: {subt}')
print(f'MULT: {mult}')
print(f'EXP: {exp}')
