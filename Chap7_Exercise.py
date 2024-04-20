# 7.1 Rental car #
# rent_car    = input('What kind of the car you would like to rent?')
# print(f"Let me see if I can find you a '{rent_car}'.")

# 7.2 Restaurant seating #
# seating_input       = input("How many people in your dinner group?")
# print(seating_input)

# seating_input       = int(seating_input)
# if seating_input > 8:
#     print('Sorry, we dont have the big table now. You need to wait for a couple time')
# else:
#     print('Your table is ready.')

# 7.3 Multiple of ten #
# input_number        = input('What is the number you would like to check?')
# input_number        = int(input_number)

# if input_number%10 != 0:
#     print(f"{input_number} is not the multiple of ten.")
# else:
#     print(f"{input_number} is the multiple of ten.")

# # 7.4 Pizza topping #
# prompt      = 'Please enter the topping you would like to add?\n'
# prompt      += '[Enter "quit" for end the program] >>> '

# topping_input   = ''
# topping         = []

# while topping_input != 'quit':

#     topping_input   = input(prompt)

#     if topping_input == 'quit':
#         print('End of adding topping.\n')
#         break
#     else:
#         print(f"You add '{topping_input}' to you pizza.\n")
#         topping.append(topping_input)

# print('Summary your pizza:')
# for pizza_top in topping:
#     print(f"\t{pizza_top}")

# 7.5 Movie ticket #
# prompt      = "How old are you?\n"
# prompt      += "[Enter 'quit' to end the conversation] >>> "

# message_input   = ''

# while message_input != 'quit':

#     message_input   = input(prompt)

#     if message_input != 'quit':

#         age             = int(message_input)
#         ticket_cost = ''

#         if age < 3:
#             ticket_cost = 'Free'
#         elif age < 12:
#             ticket_cost = '$10'
#         else:
#             ticket_cost = '$15'

#         print(f"\nYour age is '{age}'. Your ticket is '{ticket_cost}'\n") 

#     else:
#         print('------ End of program ------\n')  

# 7.8 Deli #
# sandwich_orders      = ['tuna', 'hawaiian', 'ham-cheese', 'pepperoni']
# finished_orders      = []

# while sandwich_orders:

#     finished_sandwich     = sandwich_orders.pop()
#     print(f'I have made the "{finished_sandwich}" sandwich')
#     finished_orders.append(finished_sandwich)
    
# print(f"Sandwich order: {sandwich_orders}")
# print(f"Finished order: {finished_orders}\n")

 
# # 7.9 No pastrami #
# sandwich_orders     = ['tuna', 'pastrami', 'hawaiian', 'ham-cheese', 'pastrami', 'pepperoni', 'pastrami']
# finished_orders     = []

# while sandwich_orders:

#     finished_sandwich   = sandwich_orders.pop()

#     if finished_sandwich.lower() == 'pastrami':
#         print("Deli has run out of Pastrami, we need to remove the orders.")
#         while 'pastrami' in sandwich_orders:
#             print('Remove pastrami')
#             sandwich_orders.remove('pastrami')
#         print("\n")    
#     else:
#         print(f'I have made the "{finished_sandwich}" sandwich')
#         finished_orders.append(finished_sandwich)

# print(f"Sandwich order: {sandwich_orders}")
# print(f"Finished order: {finished_orders}")

# 7.10 Dream vacation #
name_prompt     = "What is your name? >>> "
place_prompt    = "If you could visit one place in the world, where would you like to go? >>> "
continue_prompt = "Would you like to continue the pool? [Y/N] >>> "

poll_results     = {}

poll_status = True

while poll_status:
    name        = input(name_prompt)
    place       = input(place_prompt)

    poll_results[name]    = place

    while True:
        continue_poll   = input(continue_prompt)
        if continue_poll == 'Y':
            poll_status = True
            break
        elif continue_poll == 'N':
            poll_status = False
            print("-------- Poll End ----------\n")
            break
        else: 
            print('Unexpected input please enter only "Y" or "N".')
            continue

print("-------- Poll Result ----------")
for key, value in poll_results.items():
    print(f"{key} like to go to {value}")