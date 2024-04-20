import Chap8_Importfile

# 8.1 Message #
def display_message():
    print("Hi everyone, now I'm try to learn how to write 'Function' from this chapter")

display_message()

# 8.2 Favorite book #
def favorite_book(title):
    print(f"My favorite book is {title}")

favorite_book('Harry Potter')

# 8.3/8.4 T-shirt/Large shirt #
def make_shirt(size = 'Large'):
    if size in ['Large', 'Medium']:
        print(f"I love python, Make a shirt size {size}")
    else: 
        print(f"Make a shirt size {size}")

make_shirt("L")
make_shirt("M")
make_shirt()
make_shirt('Medium')

# 8.5 Cities #
def describe_city(city, country = 'Thailand'):
    print(f"{city} is in {country}")

describe_city('Newyork', 'America')
describe_city('Bangkok')
describe_city('Tokyo', 'Japan')

# 8.6 City names #
def city_country(city, country):
    print(f'"{city}, {country}"')

city_country('Newyork', 'America')
city_country('Tokyo', 'Japan')
city_country('Bangkok', 'Thailand')

# 8.7 Album
def make_album(artist_name, title, song = None):
    artist_album    = { 'artist_name': artist_name,
                        'title': title
                        }
    if song:
        artist_album['song'] = song
    
    return artist_album

beegee      = make_album('Beegee', 'Heart', 8)
beatles     = make_album('Beatles', 'Yesterday')
bodyslam    = make_album('Bodyslam', 'Inequality', 10)

print(beegee)
print(beatles)
print(bodyslam)
print('\n')

# # 8.8 User album #
# prompt_artist       = 'Please enter the artist\n'
# prompt_title        = 'Please enter the title\n'
# prompt_continue     = 'Would you like to enter other artist? [Y/N]\n'
# prompt_end          = '[Enter "q" any time to end the program]: '

# program_end         = True
# while program_end:
#     artist_input    = input(prompt_artist + prompt_end)
#     if artist_input == "q":
#         print('------- End program --------')
#         break
#     title_input     = input(prompt_title + prompt_end)
#     if title_input  == "q":
#         print('------- End program --------')
#         break

#     print(make_album(artist_input, title_input))

#     continue_check  = True
#     while continue_check:
#         continue_input  = input(prompt_continue + prompt_end)
#         if continue_input == 'Y':
#             continue_check  = False
#         elif continue_input == 'N':
#             continue_check  = False
#             program_end     = False
#         elif continue_input == 'q':
#             program_end     = False
#             break
#         else:
#             print("Wrong input please enter only 'Y' or 'N'.")

# 8.9 Messages #
def show_message(messages):
    for message in messages:
        print(message)

messages_list   = ['Hi tim', 'It has been a long day', 'Bomb!!!']
show_message(messages_list)
print("\n")

# 8.10 Sending the message #
def send_messages(messages = []):
    sent_messages   = []
    while messages:
        send_message    = messages.pop(0)
        print(f"Sending message: {send_message}")
        sent_messages.append(send_message)
    return sent_messages

sent_completes  = send_messages(messages_list)
print(messages_list)
print(sent_completes)
print('\n')

# 8.11 Archive messages #
messages_list   = ['Hi tim', 'It has been a long day', 'Bomb!!!']
sent_completes  = send_messages(messages_list[:])
print(messages_list)
print(sent_completes)
print("\n")

# # 8.12 Sandwiches #
# def sandwich_topping(*toppings):
#     """Print the list of topping that have been requested"""
#     print("-------- Topping summary --------")
#     for topping in toppings:
#         print(f"{topping}")

# sandwich_topping('ham', 'cheese', 'carrot')
# sandwich_topping('cream', 'cheese', 'strawberry')
# sandwich_topping('carrot')
# print("\n")

# # 8.13 User profile #
# def build_profile(first_name, last_name, **user_info):
#     """Build a dictionary containing everything wew know about a user."""
#     user_info['first_name'] = first_name
#     user_info['last_name']  = last_name

#     return user_info

# user_profile    = build_profile('Pattarapol', 'Sangaroon', 
#                                 University = 'Chulalongkorn', 
#                                 Company = 'Hiveground')

# print(user_profile)

# 8.14 Printing models #
user_profile    =    Chap8_Importfile.build_profile('Pattarapol', 'Sangaroon', 
                                                    University = 'Chulalongkorn', 
                                                    Company = 'Hiveground')

print(user_profile)
print(Chap8_Importfile.show_dictionary(user_profile))