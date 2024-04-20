# 6.1 Person #
person1     = {'first_name': 'Pattarapol', 'Last_name': 'Sangaroon', 'City': 'Bangkok'}
print(person1)
print(person1['first_name'])
print('\n')

# 6.2 Favorite number #
favorite_number = { 'Pat': 1,
                    'Orb': 2,
                    'Sam': 3,
                    'Yuu': 4
                    }
print(favorite_number)
print('\n')

# 6.3 Glossary #
glossary        = { 
                'List': 'Array of the value',
                'if-else': 'Condition statement',
                'Dictionary': 'Set of the list with "Key" attribute'
                }
glossary_key    = ['List', 'if-else', 'Dictionary', 'Class']
print('Glossary Meaning')
for key in glossary_key:
    print(f"{key}:\n - {glossary.get(key, 'No meaning assign')}")
print('\n')

# 6.4 Glossary 2 #
glossary['Append']  = 'Adding new element to the end of the list'
glossary['del']     = 'Delete value of the select index of the list permanently'
for key, value in glossary.items():
    print(f"{key}:\n - {value}")
print("\n")

# 6.5 Rivers #
rivers       = {
                'nile': 'egypt',
                'mississippi': 'america',
                'kong': 'thailand',
                'phaya': 'thailand'
                }
for river, country in rivers.items():
    print(f"The {river} run through {country}")

print('\nAll rivers name:')
for river in rivers.keys():
    print(river)

print('\nAll country name:')
for country in rivers.values():
    print(country)    
print('\n')

# 6.6 Polling #
friends     = ['Pat', 'Palm', 'Orb', 'Sam', 'Yuu']
for name in friends:
    if name in favorite_number.keys():
        print(f'Thank you {name} for taking the assignment.')
    else:
        print(f"I would like to invite {name} to take the assignment")
print("\n")

# 6.7 People #
person2     = {'first_name': 'Tomb', 'Last_name': 'Rider', 'City': 'Los Angeles'}
person3     = {'first_name': 'Ken', 'Last_name': 'Wannabe', 'City': 'Tokyo'}
people      = [person1, person2, person3]

for person in people:
    print('\n')
    for key, value in person.items():
        print(f"{key}: {value}")
print('\n')

# 6.8 Pets #
pet_1       = {'kind': 'cat', 'owner': 'sam'}
pet_2       = {'kind': 'dog', 'owner': 'orb'}
pet_3       = {'kind': 'fish', 'owner': 'pan'}
pet_4       = {'kind': 'dog', 'owner': 'you'}

pets        = [pet_1, pet_2, pet_3, pet_4]

count       = 0
for idx, pet in enumerate(pets):
    print(f"\nPet No.{idx + 1}")
    for kind, value in pet.items():
        print(f"{kind}: {value}")
print("\n")

# 6.9 Favorite place #
person1     = ['America', 'Thailand', 'Australia', 'China']
person2     = ['Thailand', 'Canada']
person3     = ['Yemen', 'Colombia', 'Switzerland']
person4     = ['England', 'France', 'Japan']
person5     = ['Thailand']

favorite_place  = { 'Sam': person1,
                    'Orb': person2,
                    'Pat': person3,
                    'Till': person4,
                    'Will': person5
                    }

print(favorite_place)

for person, info in favorite_place.items():
   
    if len(info) <= 1:
        print(f"\n{person}'s favorite place is:")
    else:
        print(f"\n{person}'s favorite place are:")

    for place in info:
        print(f"\t{place}")
print("\n")

# 6.11 Cities #
bangkok         = {'country': 'Thailand', 'population': 70_000_000, 'fact': 'Very hot'}
tokyo           = {'country': 'Japan', 'population': 100_000_000, 'fact': 'Animation'}
los_angles      = {'country': 'America', 'population': 10_000_000, 'fact': 'Casino'}

cities          = {'bangkok': bangkok, 'tokyo': tokyo, 'los_angles': los_angles}

print(cities)

for city, info in cities.items():
    print(f"\n{city} information:")
    for key, value in info.items():
        print(f"\t{key}: {value}")
print("\n")
        