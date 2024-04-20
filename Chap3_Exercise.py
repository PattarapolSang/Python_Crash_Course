# Exercise #

# 3.4 Guest list #
guest_list      = ['Sam', 'Tan', 'Mark']
print(f"Guest list: {guest_list}\n")

message1         = f"Hi {guest_list[0]}, I would like to invite you and your family to my party tonight"
message2         = f"Hi {guest_list[1]}, I would like to invite you and your family to my party tonight"
message3         = f"Hi {guest_list[2]}, I would like to invite you and your family to my party tonight"

print(message1)
print(message2)
print(f"{message3}\n")

# 3.5 Changing guest list #
print(f"{guest_list[2]}, cannot come to the party tonight")

cannot_come     = guest_list.pop(2)
print(f"Guest list left: {guest_list}")

guest_list.append('ham')
print(f"New guest list: {guest_list}")
print("\n")

# 3.6 More guest list #
print('We found the bigger table')
guest_list.insert(0, 'Tim')
guest_list.insert(2, 'Gus')
guest_list.append('Ken')
print(guest_list)

for guest in guest_list:
    message = f"Hi {guest}, I would like to invite you and your family to our party tonight"
    print(message)

print("\n")

# 3.7 Shrinking guest list #
print("We have only 2 left")
print(guest_list)
for pop_index in range(1,5):
    pop_guest = guest_list.pop(0)
    print(f"Sorry {pop_guest}, We need to reject your invitation")

print(f"Guest list left: {guest_list}")
del guest_list[0]
del guest_list[0]
print(guest_list)
print("\n")

# 3.8 Seeing the world #
locations       = ['japan', 'america', 'england', 'korea', 'thailand']
print(f"My wish list: {locations}")
print(f"sorted: {sorted(locations)}")
print(f"sorted(reverse=True): {sorted(locations, reverse=True)}")

locations.reverse()
print(f"reverse: {locations}")
locations.reverse()
print(f"2nd reverse: {locations}")

locations.sort()
print(f"sort: {locations}")
locations.sort(reverse=True)
print(f"sort(reverse=True): {locations}")
print("\n")

# 3.9 Dinner guest #
guest_list      = ['Sam', 'Tan', 'Mark']
print(f"Number of guests: {len(guest_list)}\n")

# 3.10 Every function #
prompt_list      = ['Bangkok', 'Chonburi', 'Lampang']
print(prompt_list[0])       # print item in the list "prompt_list" index 0
print(prompt_list[1])       # print item in the list "prompt_list" index 1

print(prompt_list[2])
prompt_list[2]   = 'Krabi'  
print(prompt_list[2])       # reassign item index 2

prompt_list.append('Lampang')           # insert to the last
prompt_list.insert(2, 'London')         # insert to the index
print(prompt_list)

pop_prompt      = prompt_list.pop(3)    # delete value and store in others
print(prompt_list)
print(f"location pop: {pop_prompt}")

del prompt_list[0]                      # just delete item
print(prompt_list)
print("\n")


print(sorted(prompt_list))                  # sort with no effect to original
print(sorted(prompt_list, reverse=True))    # sort in reverse order

prompt_list.sort()                          # sort and effect permanently
print(prompt_list)
prompt_list.sort(reverse=True)              # reverse sort
print(prompt_list)

prompt_list.reverse()                       # just reverse order
print(prompt_list)
prompt_list.reverse()
print(prompt_list)