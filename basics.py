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
###### Variables#####
#####################

print() #it prints a new line after printing the data
print("Hello World",end="!")
print(" is this working") #here above line ending with a mark rather than printing a new line

#input data from console
scan = input("Enter your age : ")
print(scan)

#there is no declaration, only assignments
#use lovercase_with_underscore for naming variables

print("yay" if 0 > 1 else "nay") #it prints nay

li = []
li.append(1) #appen new elements to an array
li.append(2)
li.append(4)
print(li)

li.pop() #delete last element
print(li)

print(li[0]) #print first index
print(li[-1]) #print last index

#li[4] => raise an IndexError


