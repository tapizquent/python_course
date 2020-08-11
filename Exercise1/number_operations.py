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
# print('what is your name? ')

# first_name = input('Input your first name: ' )
# last_name = input('Imput you last name: ')

# print()
# print('Hello, ' + first_name + ' '+ last_name + ' Welcome to addition!')
# print()

# # Ask user to input first number
# a = int(input('Input first number: '))
# # Ask user to input second number
# b = int(input('Input second number: '))

# sum = a + b
# subt = a - b
# mult = a * b
# exp = a ** b

# print()
# print(f'SUM: {sum}')
# print('SUB: ' + str(subt))
# print('MULT: ' + str(mult))
# print('EXP: ' + str(exp))

# print()

# print('New hiring process ')

# # Ask user for profession
# # Ask user for years of experience
# print('What is your profession? ')
# print('How many years of experience ? ')
# profession = input( 'What is your profession: ')
# years_exp= int(input('Years of experience: '))
# print(profession +' with '+ str(years_exp) + ' years of experience ' )


#Build a calculator in the console. Ask user for the name, print hello and the name.
#ask the user what operation they want to do. If they type 0=add, 1=sub, 2=mult, 3=div
#4=exp, 5= all  
#ask the user to imput two numbers and the numbers can be floats
#print

print('What is your name? ')
name = input('Name: ')
print('Hello ' + name )
print('What operation do you want to do? ')
print('0=add, 1= sub, 2= mult, 3= div, 4= exp, 5= all')
operation = int(input('operation: '))
a = float(input ('Number a: '))
b = float(input('Number b: '))
if operation == 5: 
    print (a+b) 
    print (a-b)
    print (a*b)
    print (a**b)
    if b!=0:
        print (float(a//b))
    else:
        print('Error ')

elif operation == 0:
    print (a+b)
elif operation == 1:
    print (a-b)
elif operation == 2:
    print (a*b)
elif operation == 4:
    print (a**b)
elif operation == 3:
    if b!=0:
        print(float(a//b))
    else:
        print('Error')
else:
    print('Good Bye ')





