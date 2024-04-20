from pathlib import Path
import json

path        = Path('.\Chap10_Exercise\learning_python.txt')
content     = path.read_text()
print(content)

print('\n--------- END CONTENT ----------\n')

lines        = content.splitlines()
for line in lines:
    print(line)

print('\n--------- 10.2 Learning C ----------\n')    

content_replace     = content.replace('Python', 'C')
print(content_replace)

print('\n--------- 10.4 Learning C ----------\n')  

prompt  = "What is your name:"
prompt  += "\n[Enter Q for quit the program] >>> "
name_list   = []

while True:

    name    = input(prompt)
    if name == 'Q':
        break
    else:
        name_list.append(name)

path_write  = Path('.\Chap10_Exercise\guest.txt')
content     = '\n'.join(name_list)
path_write.write_text(content)

check_text  = path_write.read_text()
print(check_text)

