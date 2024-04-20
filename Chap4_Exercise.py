# 4.1 Pizzas #
favorite_pizzas    = ['peperoni', 'hawaiian', 'seafood']
for pizza in favorite_pizzas:
    print(f"I like {pizza}")
print("I really love pizzas")

# 4.3 Counting to twenty #
for count in range(1,21):
    print(f"Count: {count}")

# 4.4 One to Million #
# for count in range(1, 1_000_001):
#     # print(f"Count: {count}")
print("Finished\n")

# 4.5 Summing a million #
million_list    = list(range(1,1_000_001))
print(f"Max: {max(million_list)}")
print(f"Min: {min(million_list)}") 
print(f"Sum: {sum(million_list)}")

# 4.6 Odd number #
for count in range(1, 21, 2):
    print(f"Count: {count}")

# 4.7 Three #
threes  = []
for count in range(1, 11):
    print(f"Multiple {count} --> {count*3}")
    threes.append(count*3)
print(threes)    

# 4.8 Cube #
cubes   = []
for count in range(1, 11):
    print(f"Cube {count} --> {count**3}")
    cubes.append(count**3)
print(cubes)

#  4.9 Cube comprehension #
new_cubes   = [cube**3 for cube in range(1,11)]
print(new_cubes)
print('\n')

# 4.10 Slices #
print('The first 3 items are:')
for item in new_cubes[:3]:
    print(item)

print('Three items from the middle of the list are:')
# print(len(new_cubes))
for item in new_cubes[4:7]:
    print(item)

print('The last three items in the list are:')
for item in new_cubes[-3:]:
    print(item)
print('\n')

# 4.10 My Pizzas, Your Pizzas #
print(favorite_pizzas)
friend_pizza        = favorite_pizzas[:]
print(f"My friend favorite pizzas: {friend_pizza}")

favorite_pizzas.append('chicken trio')
friend_pizza.append('tropical')

print(f"My favorite pizzas: {favorite_pizzas}")
print(f"My friend's favorite pizzas: {friend_pizza}")
print('\n')

# 4.12 More loop #
print('My favorite pizza:')
for pizza in favorite_pizzas:
    print(pizza)

print("My friend's favorite pizza:")
for pizza in friend_pizza:
    print(pizza)

print('\n')

# 4.13 Buffet
buffet_menu         = ('salad', 'cola', 'chicken', 'porks')
print(buffet_menu[1])
# buffet_menu[1]      = 'seafood'     # Try error
# print(buffet_menu[1]) 

buffet_menu         = ('ham', 'cola', 'chicken', 'seafood')
print('Change buffet menu:')
for menu in buffet_menu:
    print(menu)