# PYTHON FULL BEGINNER'S REFERENCE WITH EXAMPLES

#  ____ _____  _    ____ _____
# / ___|_   _|/ \  |  _ \_   _|
# \___ \ | | / _ \ | |_) || |
#  ___) || |/ ___ \|  _ < | |
# |____/ |_/_/   \_\_| \_\|_|


# ------ Data types --------

# String
some_name = 'Ivan Rakitic'

# Number
some_age = 24
another_age = 24.45

# Boolean
is_male = False #Always uppercase F or T, in case of False or True

# Concatenation
print("The best midfielder on the Croatian team is " + some_name + ". His age is", some_age)
# f syntax
print(f"The best midfielder on the Croatian team is {some_name}. His age is {some_age}") #Astoundingly better

# ------ Conditionals -------
if some_age != another_age:
    print('Ha! ints are never equal to floats')
elif another_age > some_age:
    print('Hmm! Now you see how floats are more powerful than ints?')
else:
    print('They are equal, I was wrong fam :(')

# ---- logical operators -----
if some_age == another_age and another_age > some_age:
    print('You will face the wrath of the floats')
elif some_age < another_age or another_age == some_age:
    print('No commento')

# ----- Taking user input -----
name = input('Enter the name of the best midfielder on the Croatian team')
if not name:
    print('Enter something if you are a true football fan!')
elif name == 'Ivan Rakitic':
    print('Hmm, you are a man of culture as well')
else:
    print(f'You have no taste, the best is certainly {some_name}')

# for loop
for x in range(11, 0, -1): # range(start, end, steps)
    print('& ' * x) 
    # In python, strings when multiplied by numbers, gives the string as many times as the number it was multiplied with

print('----------------------')

# ----- loops -----

# while loop
times = 1
while times < 11:
    print('# ' * times)
    times += 1 # times++ not working in python

# for loop
for x in range(10):
    print(x + 1)

# importing - (Importing randint from random here)
from random import randint
from random import choice as c # aliases the choice module as 'c'

# using randint
random = randint(1, 20) # inclusive of 1 and 20, picks a random number in between them
print(random)

# chooses a random choice from a list or tuple
print(c(['Lanza', 'del', 'Relampago']))

# ----- lists -------
players = ['Messi', 'Ronaldo', 'Griezmann', 'Pogba']

# counting the length of the list
print(len(players))

# ----- list methods ------

# adding an item at the end
players.append('M\'bappe')

# adding more than 1 item at the end of the list
players.extend(['Giroud', 'Ronaldo', 'Ronaldo'])

# adding an item at a particular index of a list
players.insert(2, 'Neymar')
print(players)

# removing just the last item in the list
players.pop()
print(players)

# removing an item with a particular index
players.pop(5)
print(players)

# removing a particular value in the list
players.remove('Griezmann')
print(players)

# getting the index of a particular item 
index = players.index('Pogba')
print(index)

# sorting the list in ascending order
players.sort()
print(players)

# reversing the values in the list
players.reverse()
print(players)

# counting how many times an item occurs in the list
count = players.count('Ronaldo')
print(count)

# join the items in the list with a given string
joinedPlayers = ' -- '.join(players)
print(joinedPlayers)

# slicing  -- list[start:end:step] -- End exclusive, start inclusive
slicedPlayers = players[0:5:1]
print(slicedPlayers)

# swapping values in the list
players[0], players[4] = players[4], players[0]
print(players)

# removing all items in the list
players.clear()
print(players)

# NOTE: comprehensions are just shorthand ways of generating lists, dicts, tuples, sets quickly in one line

# --- list comprehensions ------


# syntax - [placeholder.method() + 'GO' for placeholder in list_name]
gks = ['Buffon', 'Curtois', 'Ochoa', 'Neuer', 'Bravo', 'Lloris']

saver_1 = [ph.upper() for ph in gks]
print(saver_1)

# list comprehensions with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
saver_2 = [ph * 100 for ph in numbers if ph % 2 == 0] # Just if syntax
print(saver_2)

saver_3 = [num * 1000 if num % 2 == 0 else num + 10 for num in numbers] # if else syntax
print(saver_3)

# multi-dimensional lists
stri_defs = [['Aguero', 'Suarez', 'M\'bappe'], ['Ramos', 'Pique', 'Godin']]
print(stri_defs[1][1])

# looping through multi-dimensional lists
for everyone in stri_defs:
    for eachPlayer in everyone:
        print(eachPlayer + '\n')

# ------ dictionaries -------

playerTypes = {
    'striker': 'Suarez',
    'defender': 'Pique',
    'midfielder': 'Iniesta',
    'keeper': 'Ter Stegen'
}

# accessing the values from keys
stri = playerTypes['striker']
print(stri) 

# iterating through a dictionary
for v in playerTypes.values(): # values iteration
    print(v)

for k in playerTypes.keys(): # keys iteration
    print(k)

for values, keys in playerTypes.items():
    print(f'{keys}: {values}')

# conditions in dictionaries - True or False
print('keeper' in playerTypes) # alternative print('keeper' in playerTypes.keys())
print('Suarez' in playerTypes.values())

# methods in dictionaries
cup_winners = {
    'Brazil': 2002,
    'Italy': 2006,
    'Spain': 2010,
    'Germany': 2014,
    'France': 2018
}

# makes a copy of the given dictionary - stored in a separate place in memory
cup_winners_copy = cup_winners.copy()
print(cup_winners_copy['France'])
# cup_winners_copy is cup_winners -- returns False

# creates key value pairs -- Always pass an empty dictionary (would work the same way if passed -> cup_winners.fromkeys())
defenders = {}.fromkeys(['defenders'], ['Pepe', 'Ramos', 'Alba', 'Pique'])
print(defenders)

# gets the value of a key in a dictionary - doesn't give an error like cup_winners['rooster'] would give, just returns None
print(cup_winners.get('Italy'))

# clears everything in the dictionary and makes it empty
cup_winners.clear()
print(cup_winners)

# clears an item in the dictionary with a specific key
legends = {
    'Argentina': 'Messi',
    'Brazil': 'Pele',
    'Chile': 'Sanchez',
    'France': 'Zidane'
}

legends.pop('Chile')
print(legends)

# clears a random item in the dictionary
legends.popitem()
print(legends)

# updates a dictionary by using another dictionary
legends2 = {
    'Portugal': 'Ronaldo',
    'Italy': 'Buffon',
    'Germany': 'Klose'
}

legends.update(legends2)
print(legends)

# ----- dictionary comprehensions -----
numbers = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10 }

cubed_numbers = { k: v ** 3 for k, v in numbers.items() }
print(cubed_numbers)

# conditionals in dictionary comprehensions -- can be done to keys or values or both
cubed_if_even = { key : (value ** 3 if value % 2 == 0 else value) for key, value in numbers.items() }
print(cubed_if_even)

caps_if_7 = { (keys.upper() if keys == 'seven' else keys) : values for keys, values in numbers.items() }
print(caps_if_7)

sq_if_even_caps_if_3 = { (keys.upper() if keys == 'three' else keys) : (values ** 2 if values % 2 == 0 else values) for keys, values in numbers.items() }
print(sq_if_even_caps_if_3)

# ---- tuples -----

# NOTE: tuples are same as lists but are immutable and lightweight
new_tuple = ('Benzema', 'Nasri', 'Ronaldo', 'Kroos', 'Mandanda', 'Ronaldo')

# NOTE: in dictionaries, tuples can be used as keys or values, but not lists, example:
names = {
    ('Kevin', 'Lukaku'): ('Kane', 'Sterling')
}
print(names[('Kevin', 'Lukaku')])

# --- tuple methods -----

# counts the number of times an element is present in a tuple
print(new_tuple.count('Ronaldo'))

# gives the index of the particular element in the tuple
print(new_tuple.index('Mandanda'))

# looping with tuples -- same as list
for name in new_tuple:
    print(name)

# ----- sets ---------

# NOTE: sets cannot have duplicates, and they can have any random order
new_set = { 1, 4, 5, 'django', 2.444 }

# conditions in sets
print('django' in new_set)

# looping in sets
for x in new_set:
    print(x)

# converting lists to sets -- (converting list's data to have no duplicates)
some_list = ['Ronaldo', 'Messi', 'Buffon', 'Kaka', 'Ronaldo']
convert_list_to_set = set(some_list)
convert_set_to_list = list(convert_list_to_set)
print(convert_set_to_list)

# ---- set methods -----

# adds an element to the given set
# NOTE: if the element you are trying to add exists already, it won't throw an error, but the set doesn't change at all
new_set.add('Ronaldinho')
print(new_set)

# removes an element from the set, throws an error if the element is not found
new_set.remove('django')
print(new_set)

# removes an element from the set, but does not throw an error when the given element is not found
new_set.discard('bokuda')
print(new_set)

# makes a clone of the given set
# NOTE: (new_set is copied_set) will return False
copied_set = new_set.copy()
print(copied_set)

# ---- intersections and unions of sets -----

naruto = { 'Naruto', 'Sasuke', 'Sakura', 'Hinata', 'Rock Lee', 'Neji', 'Gaara', 'Madara', 'Itachi', 'Jiraiya' }
boruto = { 'Boruto', 'Naruto', 'Sasuke', 'Sakura', 'Hinata', 'Metal Lee', 'Kawaki', 'Gaara' }

# union - will return all the elements from both the sets, but won't display the duplicates
print(naruto | boruto)

# intersection - will return all the elements common in both the sets
print(naruto & boruto)

# --- set comprehension ----

squared_set = { x ** 2 for x in range(10) }
print(squared_set) # No particular order of print

caps_set = { char.upper() for char in 'Trello' }
print(caps_set) # returns a set (hence no duplicates) with one 'l' missing

# ---- functions ------

# defining a function
# NOTE: if another function with the same name is defined, python will override that function over this
def some_func(x):
    return x**2

print(some_func(4))

# default parameters -- if no power(2nd argument) provided, it will default to 1
# NOTE: here the order of the parameters matter
def exponent(num, power=1):
    return num ** power

print(exponent(4, 6)) # same result

# calling function with the name of the parameter with Keyword Arguments
# NOTE: here, since we are passing the arguments with the name of the parameters, order doesn't matter
print(exponent(power=6, num=4)) # same result

# ----- using scope -------

# global keyword -- for accessing global variables inside functions
counter = 0

def displayer():
    global counter # looks outside the scope of the function, and then finds counter in the global scope
    counter += 1
    return counter

print(counter)
print(displayer())

# nonlocal keyword -- for accessing variables in an outer function from an inner function -- for nested functions only
def outer():
    outer = 0
    print(outer)
    def inner():
        nonlocal outer
        outer += 1
        print(outer)
    inner()

outer() # prints 0 first (because if outer is not called inner will never run), then calls inner(), then prints 1

# document strings in functions -- syntax - """ This function does something """
def simple(letters):
    """ This is a simple function that prints the letters entered in caps """
    return letters.upper()

print(simple(input('Enter something: ')))

# accessing the document string
print(simple.__doc__)

# ----- *args and **kwargs --------

# *args is a parameter that accepts any number of arguments
# NOTE: returns a tuple
def sum_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all(10, 34, 56, 38, 100))

# **kwargs - keyword arguments, will accept any number of arguments with a keyword
# NOTE: returns a dictionary
def fav_teams(**name_teams):
    for x, y in name_teams.items():
        print(f'{x} likes the team {y}')

fav_teams(Asif='Portugal', Danish='Germany', Farid='Argentina')

# tuple and list unpacking to use them as arguments
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def summer(*args):
    total = 0
    for x in args:
        total += x
    print(total)

summer(*nums) # to use a tuple or list as an argument for *args parameter, just add '*' to the argument
summer(*nums2)

# dictionary unpacking to use them as arguments
fav_teams = {
    'Asif': 'Portugal',
    'Danish': 'Germany',
    'Farid': 'Argentina'
}

def fav_teams_unpack(**team_names):
    for t, u in team_names.items():
        print(f'{t} is the fav team of {u}')

fav_teams_unpack(**fav_teams) # just add '**' to the argument to unpack it to be used as an argument

# ---- lambdas -----

# one line anonymous functions - kinda like one line fat arrow functions in JavaScript

square = lambda x: x*x 
print(square(34))

# use cases of lambdas, and some inbuilt functions
# NOTE: comprehensions are preferred over lambdas(with map and filter) anyday

# using lambdas with map function
age_list = [18, 43, 19, 34, 22, 16]
age_doubler = list(map(lambda age: age*2, age_list))
for age in age_doubler:
    print(f'{age} \n')

# using lambdas with filter function
# filter function only works on basis of True and False expressions
age_odder = list(filter(lambda x: x % 2 != 0, age_list))
for odd in age_odder:
    print(odd)

# combining filter and map
names = ['Byakuya', 'Haschwald', 'Ichibei', 'Genryuusai', 'Hashirama']

filtered_mapped = list( map( lambda n: f'The name is {n}', filter( lambda n: len(n) > 7, names ) ) )
print(filtered_mapped)

# same thing now with list comprehensions
comprehended_names = [ f'The name is {n}' for n in names if len(n) > 7 ]
print(comprehended_names)


# ---- in-built functions -----

# returns True if all values are truthy, returns True when the iterable is empty
some_bool = all([ name[0] == 'H' for name in names ])
some_other_bool = all([ ])
print(f'{some_bool} and {some_other_bool}')

# returns True if any of the values are truthy, returns False when the iterable is empty
any_bool = any([ 1, 0, 0, 0 ])
any_other_bool = any([])
print(f'{any_bool} and {any_other_bool}')

# getting the byte size of a particular variable
from sys import getsizeof

a, b = [1, 2, 3], []
print(f'bytes of a: {getsizeof(a)} and bytes of b: {getsizeof(b)}')

# --- sorted inbuilt function ----
#    differs from list.sort() as:
#        can sort any iterable element
#        returns a copy of the iterable element
#        if a tuple is passed in, returns a list
#        has reverse attribute which can sort in descending order
#        has key attribute which can be used to specify the iterable in dictionaries

sorting_numbers = sorted([1, 2, 5, 22, 88, 56, 45, 67, 99])
print(sorting_numbers)
sorting_tuple_reversed = sorted((1, 2, 5, 22, 88, 56, 45, 67,99), reverse=True)
print(sorting_tuple_reversed)

sorting_dict = [
    { 'name': 'Chappy' },
    { 'name': 'Rukia' },
    { 'name': 'Byakuya' },
    { 'name': 'Zizou' },
    { 'name': 'Genryuusai' }
]

sorted_dict = sorted( sorting_dict, key=lambda name: name['name'] )
print(sorted_dict)

# ---- min and max in-built functions ----
print(max([1, 2, 3, 55, 33, 44, 0.1, 99.45]))
print(min((1, 2, 3, 55, 33, 44, 0.1, 99.45))) # tuples can also be passed

# more elaborate usage of min or max
max_char_name = max( sorting_dict, key=lambda n: len(n['name']) )
min_char_name = min( sorting_dict, key=lambda n: len(n['name']) )
print(f'MAX: {max_char_name} and MIN: {min_char_name} ')

# reversed in-built function
# different than the list.reverse() as: (same differences as between .sort() and sorted())
reverse = reversed('hello')
for rev in reverse:
    print(rev)

# ---- abs and sum and round in-built functions -----

# abs - returns the absolute value (just the magnitude without the negative)
print(abs(-3.44))

# sum - sums up the list, tuple, or any iterable passed in 
# has a start argument, whose default is 0

print(sum([1, 2, 3], 10)) # will start with 10, then add 6

# round - rounds up the given value
# has a decimal places argument, till which the value will be rounded

print(round(3.344)) 
print(round(3.5544, 2))

# ---- zip in-built function ------

# returns another iterable from other one or more iterables with all of them combined systematically
# think of it as a matrix
# NOTE: in the gathered iterables, if the shortest of them gets exhausted, then zip stops (eg: here, ', right' and 2 will not be paired)
# NOTE: the order in which the gathered iterables are put in the zip, will change the result
numero1 = [1, 2, 4, 6, 4, 2]
numero2 = [1.22, 2.44, 4.55, 4.11, 2.99]
wordo1 = ['I', 'am', 'a', 'nice', 'boi', ', right']

# from the above iterables, if we zip them(and then convert them to a list), we get:
# [(1, 1.22, 'I'), (2, 2.44, 'am'), (4, 4.55, 'a'), (6, 4.11, 'nice'), (2, 2.99, 'boi')]

# NOTE: if converting them to a dictionary, only two arguments have to be input, otherwise we get an error
# { 1:1.22, 2:2.44, 4:4.55, 6:4.11, 4:2.99 } -- if converted to a dict

print( list( zip( numero1, numero2, wordo1 ) ) )
print( dict( zip( numero1, numero2 ) ) )


# unpacking from a list and then zipping it using *args in zip
fibbonaci_nums = [(1, 3), (1, 5), (2, 8)]

print(list( zip( *fibbonaci_nums ) ))

# ---- debugging in python ------

# manually throwing an error in python (commented because after the first raise, the execution stops)
# -- raise NameError()
# -- raise ValueError('The given value doesn\'t exist')

# try and except blocks for error handling
try:
    [] + 2
except TypeError as err:
    print(err)

# try, except, else and finally for error handling
# NOTE: else runs only if try is valid
# NOTE: finally runs no matter what 
# NOTE: can have multiple exceptions of errors
try:
    num = int( input('Enter a float: ') )
    print( 4 / num )
except TypeError: 
    print('That\'s not a number')
except ZeroDivisionError:
    print('Don\'t put a zero in there!')
else:
    print('I\'ll run only if the try is valid')
finally: 
    print('You can\'t stop me from running no matter what!')

# debugging using pdb - python debugger
from pdb import set_trace

# NOTE: common pdb commands:
    # l - lists where you are in the execution
    # n - goes to the next line in the execution
    # p - print a variable
    # c - continue ( finishes debugging )

first = 'FIRST'
second = 'SECOND'
set_trace() # stops execution and opens pdb in console
fr_sec = first + second

# importing custom modules in python

from custom_random_2000 import rand
# just a self-made module which prints out a random number between 1 to 2000
print(rand())

# importing and using an external module

# using colorama and termcolor to print something in a specific color
import colorama, termcolor
colorama.init()
text = termcolor.colored('Hey, this is me in magenta', color='magenta')
print(text)



#  _____ ___ _   _ ___ ____  _   _ _____ ____
# |  ___|_ _| \ | |_ _/ ___|| | | | ____|  _ \
# | |_   | ||  \| || |\___ \| |_| |  _| | | | |
# |  _|  | || |\  || | ___) |  _  | |___| |_| |
# |_|   |___|_| \_|___|____/|_| |_|_____|____/