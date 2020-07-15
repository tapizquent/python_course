from datetime import datetime, timedelta


def get_written_weekday_from_number(number_weekday: int):
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    return switcher.get(number_weekday, "Oh oh, that's not a valid weekday")

#
# Working with Dates!
# By now we have seen a couple of different data types such as strings, ints, floats, booleans
#
# But sometimes we also want to specify Dates, such as when a record was created, a date of birth,
# or even get today's date.
#
# For this we can use `datetime` from the `datetime` package.
#
# Don't worry about packages, we'll look at this more in depth later
# but basically what they allow is to use code that someone else wrote (such as the python team)
# and apply it in our code. This makes our lives so so so much easier as we don't have to do crazy
# logic for basic actions.


# # Most data types come by default in python but `datetime` we need to import.

# # Once we import datetime, we can actually use it like this.
today = datetime.now()

# # The .now() function returns a datetime object, therefore if we want to print it,
# # we need to cast it to a string
# print('Today is: ' + str(today))

# # **IMPORT timedelta**
# # We can also do some operation with dates.
# # timedelta allows us to set a time span or time period
one_day = timedelta(days=1)

# # and we can then apply that period to other datetime to obtain a new datetime we
# # are interested in.
yesterday = today - one_day
# # Take for example the date March, 1st
# # If we want to know the date before that, 28 of Feb, what if it's a leap year?
# # This is unnecesary logic that we do not want to write!

# print('Yesterday was: ' + str(yesterday))

# # That is cool and all, but sometimes can be hard to read if we wanted to print it.

# print("Today's day is: " + str(yesterday.day))
# print("Today's month is: " + str(yesterday.month))
# print("Today's year is: " + str(yesterday.year))

# tomorrow = today + one_day

# print("Tomorrow is: " + str(tomorrow))

# # Turning datetimes into strings is fairly easy. But what if we want the user to input their birthday,
# # or a date when they want to be reminded about an activity?

# birthday_string = input('When is your birthday (mm/dd/yyyy)? ')

# birthday_date = datetime.strptime(birthday_string, '%m/%d/%Y')

# print('Birthday: ' + str(birthday_date))
# print('You were born on a: ' + str(birthday_date.weekday()))

# birthday_weekday = birthday_date.weekday()
# print('You were born on a: ' +
#       str(get_written_weekday_from_number(birthday_weekday)))

# birthday_eve = birthday_date - one_day


# print('Day before birthday: ' + str(birthday_eve))

# # Sometimes we write our code and it works great. We ask the user for input and they
# # input it in the right format and exactly what we expect.
# #
# # BUT in most cases, this will not happen. We can never expect the data to come to us
# # exactly as we want it.
# # So, we have to account for weird inputs and other errors that might arise.
# #
# # Come in: ERROR HANDLING
# #
# # Error handling != debugging
# #
# # Some examples of errors could be unknown to us in development, such as a permissions issue
# # databse changes, a server being down, amongst many other that could arise that we do not
# # have control over

# # Debugging, on the other hand, is when we run our code and it crashes, or I notice something is
# # not right

# # Syntax errors
# # Runtime errors
# # Logic errors

# # Syntax errors

# # This code won't run at all
# x = 42
# y = 206
# if x == y:
#     print('Success!!')

# # this is usually the easiest to find and track down because, as we just saw, the code
# # won't event run. And the error message we get if we run the code, will point exactly to
# # where the error is
# # This is probably the "best" type of error.

# # Runtime errors

# # This is the second "best" type of error

x = 12
y = 0
# print(x / y)

# # Here the code does not highlight in red, but as soon as we run it and we get to this expression,
# # it'll yell at me telling me that I am trying to do something that is not allowed!
# # The cool thing is that this will also let me know where the error is going on

# # When you get a runtime error, the basic strategy is to start at the line where the compiler is showing
# # and go from there

# # We can finally get into handling this errors.

# # try except!

# birthday_string = input('When is your birthday (mm/dd/yyyy)? ')
# birthday_date = datetime.strptime(birthday_string, '%m/%d/%Y')

# try:
#     birthday_string = input('When is your birthday (mm/dd/yyyy)? ')
#     birthday_date = datetime.strptime(birthday_string, '%m/%d/%Y')
# except:
#     print('Format inputted is not correct. Please try again in format: mm/dd/yyyy')

# first_name = input('What is you name? ')
# last_name = input('What is you name? ')
# print('Hello ' + last_name)

# # Error handling is not used to find Bugs
# #
# # But what is a bug?
# #
# # A bug might be when I know that the code won't run if I follow a particular path
# # or do certain action.
# # But the point is that we (the developer) have control over it

# # But if this is something where a server might be down or when I'm getting input from a user
# # then this is considered an error that I will want to try except

# # We don't have to catch every error.
# # That is, if we are not going to log the error, or if we are not gonna `exit gracefully`,
# # we can just let the error be.

# # "But that might cause my application to crash!"
# # Well, yes. But sometimes that is what we want. If our application ends up in a state
# # where we don't know what happend or it's not where it's supposed to be. Well, let it crash.

# # Lastly, we have

# # Logic errors:

# # Code compiles compiles properly, so theres not syntax error, it doesnt give us an error message
# # so there are no runtime errors, it just doesn't give us the respose we're looking for

x = 206
y = 42
if (x > y):
    print(str(x) + ' is greater than ' + str(y))


# # Side note: we will take a look in the future at Unit Testing and Test Driven Development (TDD) which consists
# # of writing small automated scripts that makes sure our code does what it is expected to do.

# # So again,
# # Figuring out what went wrong:
# #
# # Stack trace:
# # - Last calls are on the top
# # - Your code is likely on the bottom
# # - Seek out line numbers
# #
# # Finding your mistake:
# # - Re-read your code
# # - Check the documentation -- Either by hovering over the function/method you're using or python/package website
# # - Search the internet -- Stack Overflow and Google are your best friends
# # - Take a break
# # - Rubberducking
# # - Ask someone for help
