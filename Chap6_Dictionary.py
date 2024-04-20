# Nesting #
alien_0     = {'color': 'green', 'point': 5}
alien_1     = {'color': 'yellow', 'point': 10}
alien_2     = {'color': 'red',  'point': 15}

aliens      = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n')

# Make an empty list for storing aliens
aliens       = []

# Make 30 green aliens #
for alien_number in range(30):
    new_alien   = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[-5:]:
    print(alien)

print(f"Number of total aliens create: {len(alien)}")
print('\n')

# Change attribute #
for alien in aliens[-3:]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'

for alien in aliens[-5:]:
    print(alien)