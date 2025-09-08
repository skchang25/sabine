#File: homework1.py
# --- Variables and Data Types ---
def vtype(x):
    print(x)
    print(type(x))

a=10
vtype(a)
#integer, a whole number without a decimal point

b =1.5
vtype(b)
#float, a number including a decimal point (this deciaml can be 0)

c=3j
vtype(c)
#complex, a number comnatinign real parts and imaginary parts, denoted by j

d=("hello")
vtype(d)
#string, sequence of multiple characters forming text

e=[1,2,3]
vtype(e)
#list, multiple values stored in sequential order under one variable

f={"name": "Ellen", "favorite fruit": "strawberry"}
vtype(f)
#dict, Dictonary, storing data with key and answer pairs. Ex. "name " is the key and "Ellen" is the answer.

g=(1,2)
vtype(g)
#tuple, an immutable variable storing multiple ordered values under one variable.

h=["apple","bannana","strawberry"]
vtype(h)
#list

i=True
vtype(i)
#Boolean, returns True or False depending on assesed statment

j = None
vtype(j)
#NoneType, Default return for python when nothing exist, as in an empty statment or not return from a function.

k=[True,"blue",12]
vtype(k)
#list

vtype(str(14))
#str

vtype(1e4)
#float

vtype(range(3))
#Range, offers a immuntable sequence of numbers iterating up to the inputed value.

# 1. Nine variable types.
# 2. Int, float, str, dict, tuple, list, noneType, boolean and complex.
# 3. m and b are floats, d and l are strings, e, h and k are lists.
# 4. Covert the number passed is to a string value itself, 14 becomes '14'.
# 5. Range: creating a range from 0 to the inputted value, often used in iteration.

# -- Booleans

print(10>9) # True, 10 is greater than 9
print(10==9) # False, 10 is not equal to 9
print(10<=9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, the string is not empty.
print(bool(123)) # True, a non empty string evealuates to true
print(bool(["apple", "cherry","bannana"])) # True, non-empty list.
print(bool(True)) # True, the boolean true is true, true is a boolean value.
print(bool(False)) # True, the boolean false evaluates to true, false is already a boolean value
print(bool(0)) # True, existing input that does not leave the input empty
print(bool(" ")) # False
print(bool(())) # False, empty input
print(bool([])) # False, empty list
print(bool({})) #False, empty input
print(bool(True and False)) # False, True and False cannot both be True
print(bool(True and True)) # True, True and True is true.
print(bool(False and False)) # False, second statment will never be reached and values align
print(bool(not(False))) #True, not false evaluates to true
print(bool(not(True))) #False, not false is true.

# 1. Statments passing through boolean assesements lacking arguemtns will pass as false, and True will return for any exisitng valid variaible input.
# 2. bool(False) evluating if the datatype is a boolean versus which boolean.
#3.
print(6%2 ==0) # True, 6 is evenly divided by 2 and therefore the remainder is equal to 0 and the statement is true.
#4.
print(5%2 ==0) # False, 5 is not evenly divisible by 2, therefore there will be a non-zero remainder when mod is invovoked, makign the equivalency untrue.

# -- Operators 

print(10+5) # 15: addition
print(10-5) # 5: subtraction
print(2*4) # 8: multiplication
print(6/3) # 2.0:division of floats
print(5%2) # 1: mod, determines the remaining value after the maximum number of times the second value can evenly go in to the first number is taken away. (ex. 5 % 2, 2 evenly goes into 5 twice, where 5-4 = 1, returns 1).
print(3**2) # 9: power function, first number to the power of the second value.
print(15//2) # 7: Floor division, performs division, however decimals are truncated and the returned answer is an integer.
print(5==2) # False: compares two values to see if they are equivalent, returns a boolean.
print(10!=10) # False: compares two calues to determine if they are not equivalent, returns a boolean.
print(2<5) # True: less than comparison, returns a boolean.
print(12>5) # True: Greater than comparison.
print( 5<=6) # True: less than or equal to comparison.
print(1>=10) # False: Greater than or equal to comparison.

#-- Assignment Operators

x=5
x +=5 #Sets x to be the existing value of x plus 5
x -=4 #resets x to be the value of x currently minus 4
x *=3 # resets x to be the current value of x multipled by 3.
print(x)

#-- Logical Operators

#1. "and " creates a situation in which to evaluate to True, both values must agree.
print(4%2 == 0 and 6%3 ==0) #True
print(5%2 ==0 and 6%3 ==0) #False
#2. The "or" operator creates a situation where one or both of the statments can evaluate to true for the statment to be true, the do not have to agree.
print(8%2 ==0 or 7%2 ==0) # True, the first equivalence resolves true, the second false.
print(9%2 ==0 or 5%2 ==0) # False, both equations resolve to false.
#3. The "not" operator returns to boolean value the input is not, if the input where true, it returns false and vice versa.
print(not(4%2==1)) # True, not(False) resolves to true.
print(not(4%2==0)) # False, not(True) resolves to false.

# -- More Questions

#1. A single slash is a typical division performed, leaving decimals in the final answer and returning a float. The double slash indicates floor division, which divides the two values and truncates the decimals, leaving only th integer portion of the answer that is also not nessesarily rounded.
#2. The percent sign is a mod action, mod checks how many times the second input ccan evenly fit into the first input and returns the amount left over while floor divion returns the integer portion of the other factor within the first value.
#3. The mod (%) operator would tell you only the remaining value after the maximum times the divisor can fit into the divisee. For example, if the equation 5%2 were to be executed, the returned value would be one as 2 can fit into 5 twice, leaving one as the remainder.
#4. Assignment operators are able to assign and manipulate variables. An equals sign alone will assign whatever the righthand side of the equation is to the variable, using an assignment operator with a +,-,* would take the currently set value of the varaible and reset it to itself and the righthand side of the equation (x+=1 == x=x+1).

# --Strings

my_string = 'hello'
print(my_string) #Prints: hello
print(my_string[0]) #Prints the 0th letter of my_string == h
print(my_string[1]) #Prints:e
print(my_string[2]) #Prints:l
print(my_string[3]) #Prints:l
print(my_string[4]) #Prints:o
print(my_string[-1]) #Prints:o
print(my_string[1:3]) #Prints:el
print(my_string[1:5:2]) #Prints:el
print(len(my_string)) #Prints: 5
print(my_string+(" goodbye")) #Prints: hello goodbye
print(my_string*7) #Prints: hellohellohellohellohellohellohello

# -- Questions:
#1. Slicing allows python to access as spesifc section of a string. Within the last tests, this would have been invoked using [1:3] and [1:5:2], we are also able to access indivisual values of a string.
#2. The variable 'name' is assigned "Oski". Within the print statment, the string written in the print statment within the quotations is printed first, then the secod value, the 'name' varaible is called and prints the string "Oski".
name = "Oski"
print("Hello, my name is", name)
#3. The variable "name" is assigned the string "Oski". The print statment pritns the strings written and calls the variable 'name', which results in printing the name 'Oski'
name = "Oski"
print(f"Hello, my name is {name}")
4. The first is a way to imbed the string inside 'name' into the string itself to be printed, the second will print a repersentation of the variable.

# -- Terminal Commands

#cd: Changed directories, moves from one folder to another. Example: cd Desktop
#ls: lists the contents of a directory. Example: ls (when used as the first line will display the contents of the User folder, or all exiting folder on the computer).
#ls -a: lists information about directories and folders within the current directory. Example: ls -a (when used as the first command will display all folders and coding software, informatiosn and histories the computer uses).
#mkdir: Creates a new folder in the existing directory. Example: mkdir homework_1
#cat:
#pwd: displays the path taken to get to a certain folder or file through all previous directories. Example: pwd ( as the first line will return the User file, pwd used after the homework_1 folder would display the User folder, Python_Decal_Fa25, yourname folder, and then homework_1).
#cd ..: Returns to one directory above the current directory (towards the parent directory). Example: cd.. (used after the yourname folder would take you to the Python_Decal_Fa25 folder).
#cd .: 
#cd ~:



