from restaurant import Restaurant
from user import User
import admin

my_KFC  = Restaurant('KFC', 'Fast food')
my_KFC.describe_restaurant()

my_user = admin.Admin('Pattarapol', 'Sangaroon')
my_user.greet_user()
my_user.privilege.show_privilege()