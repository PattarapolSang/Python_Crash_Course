from name_function import get_formatted_name

print("Enter 'q' for exit at ant time")

while True:

    first   = input("\n Please give us your first name: ")
    if first == 'q':
        break

    last    = input("\n Please give us you last name: ")
    if last == 'q':
        break

    formatted_name  = get_formatted_name(first, last)
    print(f"A neatly you full name is {formatted_name}")

    