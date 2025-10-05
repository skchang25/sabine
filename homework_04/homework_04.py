foods = ["Strawberry","Blueberry","bananna","mango","blackberry"]
#1
print(foods[1])
#2
print(foods[-1])
#3
foods.append("Pineapple")
#4
foods.insert(1,"apple")
#5
foods.remove("bananna")
#6
print(len(foods))
#7
for food in foods:
    print(food.upper())
#8
new_foods = [foods[0::5]]
print(new_foods)
#9
potato = False
for food in foods:
    if food == "potato":
        potato = True
if potato == True:
    print("A potato!")
else:
    print("No potato")


#3.2

list = []
for i in range(0,21):
    list.append(i)
print(list)

#1
def get_first_15(numbers):
    return numbers[0:15]

print(get_first_15(list))

#2
def get_every_5th(lst):
    return lst[::5]

print(get_every_5th(list))

#3
def reverse_and_stride(lst):
    return get_every_5th(get_first_15(lst))[-1::-3]

print(reverse_and_stride(list))

#3.3

numbers = [[1,2,3],[4,5,6],[7,8,9]]
#1
print(numbers[2])
#2
print(numbers[1][1])
#3
numbers.append([10,11,12])
#4
def sum_nested():
    sum =0
    for row in range(len(numbers)):
        for col in range(0,len(numbers[row])):
            sum += numbers[row][col]
    return sum
print(sum_nested())


#3.4
list =[]
temp_list = []
value = 1
for row in range(0,5):
    list.append([])
    for col in range(0,5):
       list[row].insert(col,value)
       value += 1
print(list)

#1
def multiples_of_3(list):
    for row in range(len(list)):
        for col in range(len(list[0])):
            if list[row][col] % 3 == 0:
                list[row].pop(col)
                list[row].insert(col,"?")
    return(list)
    print(list)

#2
def sum_of_not_three(list):
    List = multiples_of_3(list)
    sum = 0
    for row in range(len(List)):
        for col in range(len(List[0])):
            if List[row][col] != "?":
                sum += List[row][col]
    return sum
    print(sum)

#4.1
ages ={"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}
#1
print(ages["Katie"])
#2
ages["Mira"] = 100
#3
ages["Milana"]=52
#4
del ages["Milana"]
#5
for person,age in ages.items():
    print(f"{person} is {age}")

def favorite_function():
    print(f"Given the list: [{list}, the sum_of_not_three() function will return {sum_of_not_three(list)}")

favorite_function()