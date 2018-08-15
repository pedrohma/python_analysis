# Lists
shopping_list = [ "milk", "cheese", "bread" ]

for item in shopping_list:
    if "milk" in shopping_list:
        print("Delicious!")

    if "eggs" not in shopping_list:
        print("Well we can't have that!")
        shopping_list.append("eggs")

# Creating Dictionaries
foods = {}
foods["banana"] = "A delicious and tasty treat!"
foods["dirt"]   = "Not delicious. Not tasty. DO NOT EAT!"
print(foods)

if "cheese" not in foods:
    foods["cheese"] = "Cheese is one of the known foods!"
    print(foods["cheese"])

# Adding lists to Dictionaries

ingredients = {}
ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]
print(ingredients)

europe = []
germany = {"name": "Germany", "population": 81000000}
europe.append(germany)
luxembourg = {"name": "Luxembourg", "population": 512000}
europe.append(luxembourg)
print(europe)
