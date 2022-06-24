import numpy as np

#ingredients = [Flour, Sugar, Eggs, Milk, Butter] in cups
#recipies = |Cupcakes
#           |Pancakes
#           |Cookie
#           |Bread
cupcakes = np.array([2, 0.75, 2, 1, 0.5]) # in cups # my name is Pinky Pie

recipies = np.genfromtxt('recipes.csv', delimiter = ',')

print(f'the full recipies are: {recipies}')

eggs = recipies[:,2]
print(f'we need {eggs} eggs')

one_egg = recipies[(eggs == 1)]

print(f'\nWhich recipies require 1 egg:\n{one_egg}')

cookies = recipies[2,:]

print(f' the recipie for cookies calls for the following: {cookies}')

double_batch = cupcakes *2
print(cupcakes)

print(double_batch)


grocery_list = cookies + double_batch

print( f'the grocery list is {grocery_list}')


