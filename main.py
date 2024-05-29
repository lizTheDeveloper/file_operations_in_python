example_file = open("example_file.txt", "r")

file_contents = example_file.read()

example_file.close()

print(file_contents)

ingredient_costs = {
    "flour": 2.5,  # per kg
    "sugar": 1.5,  # per kg
    "butter": 3.0,  # per kg
    "water": 0.01,  # per liter
    "salt": 1,  # per kg
    "yeast": 0.05,  # per oz
    "eggs": 0.2,  # per egg
    "milk": 0.8,  # per liter
    "chocolate_chips": 4.0,  # per kg
    "vanilla_extract": 20,  # per liter
    "baking_powder": 0.02,  # per gram
    "baking_soda": 0.015,  # per gram
    "cinnamon": 0.03,  # per gram
    "raisins": 5.0  # per kg
}

import json

ingredient_cost_file = open("ingredient_costs.json", "w")

ingredient_cost_file.write(json.dumps(ingredient_costs))

ingredient_cost_file.close()


## convert the json to a csv
## open data.csv in append mode
data_csv = open("data.csv", "a")

## loop over the ingredient_costs dictionary
for ingredient_name,amount in ingredient_costs.items():
    ## make the ingredient and amount become a string, like this: flour,2.5
    ingredient_string = "\n" + ingredient_name + "," + str(amount)
    ## append the string to the end of the csv file
    data_csv.write(ingredient_string)

data_csv.close()

