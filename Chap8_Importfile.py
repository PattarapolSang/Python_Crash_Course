# 8.12 Sandwiches #
def sandwich_topping(*toppings):
    """Print the list of topping that have been requested"""
    print("-------- Topping summary --------")
    for topping in toppings:
        print(f"{topping}")


# 8.13 User profile #
def build_profile(
            first_name, last_name, 
            **user_info):
    """Build a dictionary containing everything wew know about a user."""
    
    user_info['first_name'] = first_name
    user_info['last_name']  = last_name

    return user_info

def show_dictionary(dic_info):
    """Print the key and value in dictionary"""
    for key, value in dic_info.items():
        print(f"{key}: {value}")
    