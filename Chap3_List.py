# Access element in the list #
bicycles    = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

# Start index #
print(bicycles[1])                  # index start from 0
print(bicycles[3])

print(bicycles[-1])
print(bicycles[-4])

# Using individual from list #
message     = f"My first bicycle is {bicycles[0].title()}"
print(message)

# Modifying element in a list #
motorcycles     = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]  = 'ducati'          # Modify element index 0
print(motorcycles)

# Add element to the list
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')         # Add element to the last
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')     # Add element to index
print(motorcycles)

# Remove element from list #
del motorcycles[0]                  # Delete element by index
print(motorcycles)

popped_motorcycle   = motorcycles.pop() # Delete element and store in variable
print(motorcycles)
print(popped_motorcycle)

last_owned  = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles     = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned     = motorcycles.pop(0)
message         = f"The first motorcycle I owned was a {first_owned.title()}"
print(message)

motorcycles.append('ducati')
motorcycles.append('honda')
print(motorcycles)

too_expensive   = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
message         = f"\nA {too_expensive.title()} is too expensive for me."
print(message)


