T = int(input())
for c in range(T):
    num_ingredients, num_portions, desired_portions = (int(x) for x in input().split())

    scaling_factor = desired_portions/num_portions
    ingredients = []
    index_of_main_ingredient = -1
    for i in range(num_ingredients):
        name, weight, percentage = input().split()
        ingredients.append([name, float(weight), float(percentage) ])
        if float(percentage) == 100:
            index_of_main_ingredient = i


    scaled_weight_of_main_ingredient = ingredients[index_of_main_ingredient][1]*scaling_factor

    for i in range(num_ingredients):
        if i == index_of_main_ingredient:
            ingredients[i][1] = scaled_weight_of_main_ingredient
        else:
            ingredients[i][1] = scaled_weight_of_main_ingredient*ingredients[i][2]*10**-2

    print(f"Recipe # {c+1}")
    for ingredient in ingredients:
        print(ingredient[0], ingredient[1])
    for _ in range(40):
        print("-", end="")
    print()
    
