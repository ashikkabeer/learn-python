#started learning python
print('hello world')

#primitives
print(1+1) #simple addition
print(5//3)    #division result rounded down
print(2**3) #exponent

print(not True) #negate with `not`
print(True and False) 
print(True or False)

#value of true is 1 and false is 0. So True + True gives 2;

print(0==False) #returns true becaus 0==0;
print(bool(0)) # None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

#seeing whether a value is in range
print('valies in range')
print(1 < 2 and 2 < 3)

# is chceks if 2 variables refer same objects
# == checks if the objects pointed to have the same values

a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(b)
print(b is a) #returns false because values same, different objects
print(b == a)

#STRINGS

first = "hello"
second = 'world'

print(first +" "+ second)
print(first[0]) #string can be treated like strings
print('Ashik'[1])
print(len(first)) #length of the string

print(f"She said {first}") #formatted string literals

#None is an object

#####################
##### Variables #####
#####################

print() #it prints a new line after printing the data
print("Hello World",end="!")
print(" is this working") #here above line ending with a mark rather than printing a new line

#input data from console
#scan = input("Enter your age : ")
#print(scan)

#there is no declaration, only assignments
#use lovercase_with_underscore for naming variables

print("yay" if 0 > 1 else "nay") #it prints nay

li = []
li.append(1) #appen new elements to an array
li.append(2)
li.append(4)
li.append(5)
li.append(6)
li.append(7)
li.append(8)
li.append(9)
li.append(10)
print(li)

li.pop() #delete last element
print(li)

print(li[0]) #print first index
print(li[-1]) #print last index

#li[4] => raise an IndexError

print(li[1:8]) #returns value from index 1 to 8
print(li[2:]) #returns from 2nd to last index
print(li[::2]) #returns list selecting every second entry
print(li[::-1]) #returns list in reverse order

li2 = li[:]
print(li2)

del li[2] #remove arbitrary elements
print([li])

li.remove(2) #removes the value, if value not found, raises a value error
print(li)

li.insert(3,4) #inserted 3 in index 4
print(li)

li.index(5) #returns the index of the value.

li3 = ['q','w','e','r','t','y']
print(li + li3) #concatenated two lists
li.extend(li3) #concatenated two lists using extends()
print(li) 
print('q' in li) #checks elements in the list
print(len(li)) #length of the list

###TUPLES###
#tuples is like a list, but are immutable

tup = (1,2,3)
print(tup[0])

print(type((1,)))
len(tup) 
print(tup + (4,5,6)) 
# You can do most of the list operations on tuples too
a, b, c = (1,2,3) #a=1, b=2, c=3
print(a) 
print(b)
print(c)

##################
###Dictionaries###
##################

dict = {"one" : 1, "two" : 2, "three" : 3}
print(dict["one"])

#dictionaries store mappings from keys to values
#keys for dictionaries have to be immutable typws
#immutable types includes ints, floats, strings, tuples

print(list(dict.keys())) #get all keys as an iterable with keys()

print(list(dict.values())) #get all values as an iterable with values()
print("one" in dict) #check for the existance

dict.setdefault("five",5) #insert into dictionary if the key isn't present
print(list(dict.keys()))

dict.update() # another way to add
del dict["one"] #delete the key one
print(dict)

someSet = {1,1,2,2,3,3,4,4,5,5,6,6,7,7} #set store the well sets
print(someSet) #print {1, 2, 3, 4, 5, 6, 7}

someSet.add(8) #add elemets
print(someSet)

################################
###Control Flow and Iterables###
################################

var = 50
if var > 10:
    print(f"{var} is bigger than 10" )
else:
    print(f"{var} is smaller than 10")

for animal in ["dogs", "cat", "mouse"] :
    print("{} is a mammal".format(animal)) #format() to interpolate formatted strings

for i in range(5): # prints number from 1 to 5
    print(i)

for i in range(5,10): # prints number from 5 to 9
    print(i)

print("for loop")

for i in range(4, 19, 3) : #range(lower,upper,step)
    print(i)

animal = ["dog","cat", "mouse"]
for i, value in enumerate(animal):
    print(i,value)

x=0
while(x < 4):
    print(x)
    x = x +1

try:
    raise IndexError("this is index error")
except IndexError as e:
    pass
else:
    print("All good")
finally:
    print("cleaned up resouces")
