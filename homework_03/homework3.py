def say_goodbye(name):
	print("Goodbye",name)
	#takes name and prints the variable value with the string "goodbye"



def print_circle_area(radius):
	print(pow(radius,2)*(3.14))
# squares inputted radius and multiplies by pi



def subtract(a,b):
	return a-b
# subtracts second input (b) from first input (a)



def multiply(a,b):
	return(a*b)
# multiplies first and seconds input



def divide(a,b):
	return(a/b)
# divides first input (a) with seconds input (b)


def what_to_wear(temps):
	return(min(temps),max(temps))
# uses the built in min and max functions to locate and return the lowest and highest values from the temperature list.



def is_weekend(DoW):
	#DoW = day of week
	if DoW == 6 or DoW == 7:
		return True
	else:
		return False
# uses an condtional if, else statment to test if if the inputted day of the week is equivalent to a weekend day.



def Fuel_effeciency(miles,gallons):
	return(miles/gallons)
# divides the miles input by the gallons input to return the final efficiency


def secret_code(int):
	counter = 0
	original_code = int
	while int>0:
		if int != 0:
			counter += 1
			int = int //10
			# iterates through the original code with floor division be 10. When counted each time this will set the counter to how many characters are in the number.
	firstNum = (original_code/10- original_code //10)*10
	# the first num is calculated by dividing the original code by ten, and subtracting the floor divised num, leavign the first num in decimal form, which is multipled by ten to get the correct placement.
	finalNum = ((original_code //10)*pow(10,-(counter-1))+firstNum)*pow(10,counter-1)
	# the original code id floor divided by ten and then multiplied by 10 to the neagtive power of one minus the counter to create a decimal version of the number with the first num. This is then added to the first number, and multipled by 10 to the power of counter minus one to place all characters in the correct places.
	int_finalNum = round(finalNum)
	# the final answer is a decimal, so to create an integer, the .0 if rounded to the nearest int
	return (int_finalNum)



def power_operator(base,power):
	val = 1
	for i in range(power):
		i = base
		val *= i		
		# the val is the final returned number, the iteration in the for loop continues for the length of power, and multiplies the base value once every iteration.
	return val


def min_value(listNums):
	val = listNums[0]
	# the value is set to the first value of the list
	for min in listNums:
		if min < val:
			val = min
			# while iterating through the list if any num in the list is smaller than the first val of the list, the valuse is replaced with said num, and continues comparing for the rest of the list
	return val


def max_value(listNums):
        val = listNums[0]
        for max in listNums:
                if max > val:
                        val = max
        return val
	# similar to the min_value, however the conditional changes to check if the number is larger than the current val value


def min_value_whileLoop(listNums):
	min = listNums[0]
	l = len(listNums)
	counter =1
	while l>0:
		if min>listNums[counter]:
			min = listNums[counter]
		l -= 1
	return min
	# similar logic to the max_value def, however the duration of the while loop is determined by subtracting one from the length of nums after every iteration and ceases to run when the len value reaches 0.
print(min_value_whileLoop([1,2,3,4,5]))

def max_value_whileLoop(listNums):
	max = listNums[0]
	l= len(listNums)
	while l>0:
		if max<listNums[l-1]:
			max = listNums[l-1]
		l -= 1
	return max
	# similar logic as the min_value_whileLoop() and the max_value() def, the val is compared to every one in the list and is replaced if the conditon that the value in the list is larger than the current max for the duration of the length ( the value len-1 is used as the length value does not include the 0 offest that appears in the list, and is then manually added).



def Calculate_the_sum(int):
	sum =0
	while int >0:
		sum += (int/10 - int//10)*10
		int = int//10
	return round(sum)

# for the length of any int, the int is divided by ten and the floor divised value of the int is subtracted from the first value to produce the decimal version of the last character in the number, which is then multiplied by ten, and added to the sum, as the original int and is reset to itself floor divided by ten to repeat the process for the duration of the length of the num.

def print_results(int):
	print("int =", int)
	print("result", secret_code(int))
	print(f"The result of Secret Code (5.4) with int = {int} is {secret_code(int)}]")

print_results(1369)

