# declare and assign total number of types of people
types_of_people = 10
# print out the value of types_of_people
x = f"There are {types_of_people} types of people."

# declare and assign binary
binary = "binary"
# declare and assign do_not
do_not = "don't"
# print out both binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# print x
print(x)
# print y
print(y)

#print formated string including variable x
print(f"I said: {x}")
# print formated string including cariable y
print(f"I also said: '{y}'")

#declare false
hilarious = True
# declare cvariable joke_evaluation with formated variable Hilarious
joke_evaluation = "Isn't that joke so funny?! {}"

# print the formated string variable above
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with the right side."

# printing concatenated variables
print(w + e)
