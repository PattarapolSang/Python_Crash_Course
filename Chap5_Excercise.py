# 5.2 More condition test #
string1     = 'Sam'
string2     = 'Ham'
print(string1 == string2)
print(string1 == 'Sam')

print(string1 == 'sam')
print(string1.lower() == 'sam')

num1        = 1
num2        = 2
num3        = 3
print(num1 == 1)
print(num1 != num2) 
print(num2 > num1)
print(num2 < num3)
print(num3 >= 3 or num2 > num1)

print(num3 <=3)  

print(num3 >= 3 and num3 > num2)
print(num1 == num2)
foods     = ['porks', 'chickens', 'seafoods', 'fish', 'squid']
print('mushroom' in foods)
print('mushroom' not in foods)
print('\n')

# 5.3 Aliens color 1 #
shutdown_alien     = 'b'
if shutdown_alien == 'red':
    print('You got 5 points')
if shutdown_alien == 'green':
    print('You got 2 points')
if shutdown_alien == 'blue':
    print('You got 1 points')

# 5.4 Aliens color 2 #
if shutdown_alien == 'red':
    print(f"You shoot down {shutdown_alien}, you got 5 points")
elif shutdown_alien == 'green':
    print(f"You shoot down {shutdown_alien}, you got 2 points")
elif shutdown_alien == 'blue':
    print(f"You shoot down {shutdown_alien}, you got 1 points")  
else:
    print('Error in the system')  

# 5.6 Stage of life #
age_input   = 60
if age_input < 2:
    print(f'Your age is {age_input}. You are "Baby"')
elif age_input < 4:
    print(f'Your age is {age_input}. You are "Toddler"')
elif age_input < 13:
    print(f'Your age is {age_input}. You are "Kid"')
elif age_input < 20:
    print(f'Your age is {age_input}. You are "Teenager"')
elif age_input < 65:
    print(f'Your age is {age_input}. You are "Adult"')
else:
    print(f'Your age is {age_input}. You are "Elder"')
print("\n")

# 5.7 Favorite fruit #
favorite_fruits     = ['Banana', 'Apple', 'Mango', 'Melon'] 
check_fruit         = ['Tomato', 'Berry', 'Pineapple', 'Apple']

for fruit in check_fruit:
    if fruit in favorite_fruits:
        print(f"Yes, {fruit} is my favorite fruit")
    else:
        print(f"No, {fruit} is not my favorite")
print("\n")

# 5.8/5.9 Hello admin/No user #
usernames       = ['Admin', 'Tim', 'Pat', 'Peter']
# usernames       = []
if usernames:
    for user in usernames:
        if user == 'Admin':
            print(f"Hello {user}, would you like to see the status report.")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some user.")
print('\n')

# 5.10 Checking username #
current_usernames       = ['Admin', 'Tim', 'PAT', 'Peter']
new_users               = ['Admin', 'Kan', 'Pat', 'Orb']

# Clear case sensitive #
current_usernames_lower = []
for user in current_usernames:
    current_usernames_lower.append(user.lower())
print(current_usernames_lower)    

for user in new_users:
    if user.lower() in current_usernames_lower:
        print(f"This name {user} has been used already. Please enter the new name.")
    else:
        print(f"This name {user} is available.")
print("\n")

# 5.11 Ordinal number #
numbers     = list(range(1,11))
print(numbers)

for num in numbers:
    if num == 1:
        print(f"{num} --> {num}st")
    elif num == 2:
        print(f"{num} --> {num}nd")
    elif num == 3:
        print(f"{num} --> {num}rd")
    else:
        print(f"{num} --> {num}th")
print("\n")