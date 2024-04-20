from pathlib import Path
import json 

# 10.6 Addition #

prompt          = 'Please enter your input: '
sum_number      = 0

while False:

    try:
        number  = input(prompt)
        if number == 'Q':
            break
        number  = int(number)
        print(f"Your new number input is {number}")
        sum_number  += number
    except ValueError:
        print('Input should be number')

print(f"Your sum number is {sum_number}\n")

# 10.7 Cats and Dogs #

directories     = ['.\Chap10_Exercise\cat.txt', '.\Chap10_Exercise\dog.txt', 'dog.txt']

for directory in directories:
    try:
        path    = Path(directory)
        content = path.read_text()

        print(f"Reading text from file directory '{directory}'")
        print(content)
        print('End reading\n')

    except FileNotFoundError:
        # print(f"Can not find a file in directory '{directory}'")
        print()

# Storing Data #

username        = input('What is your name: ')

path        = Path('username.json')
content     = json.dumps(username)

path.write_text(content)

print(f"We'll remember you when you come back, {username}")

read_content    = path.read_text()
print(read_content)
read_content        = json.loads(read_content)
print(read_content)


