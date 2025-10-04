foods = ["Strawberry","Blueberry","bananna","mango","blackberry"]
print(foods[1])
print(foods[-1])
foods.append(["Pineapple"])
foods.insert("apple",1)
foods.remove("bananna")
print(len(foods))
for food in foods:
    print(food.upper())
new_foods = [foods[0],foods[-1]]
