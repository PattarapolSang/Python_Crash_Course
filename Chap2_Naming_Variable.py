# Name and variable #
message = 'Hello world!222'
print(message)

message = 'Hello world new line'
print(message)

# Changing case and string method #
name = "ada lovelace"
print(name.title()) # First letter to the uppercase
print(name.lower()) # All character to the lowercase
print(name.upper()) # All character to the uppercase

# Using variable as string #
first_name  = "ada"
last_name   = "lovelace"
full_name   = f"{first_name} {last_name}" # f stand for 'format' string

print(full_name)
print(f'Hello, {full_name.title()}')

message     = f"Hello, {full_name.title()}"
print(message)

# Adding white space to String with Tab or newlines #
print("\tpython") # Add \t for Tab
print("Language:\nPython\nC\nJavascript") # Add \n for new space

print("Language:\n\tPython\n\tC\n\tJavascript")

# Stripping white space #
favorite_language   = '   python is great '         # Have space at first and last
strip_lan           = favorite_language.strip()     # Remove all first and last
print(favorite_language)
print(favorite_language.rstrip())                   # Remove only last (Right)
print(favorite_language.lstrip())                   # Remove only first (Left)
print(strip_lan)                                    # Remove all first and last

# Remove prefix #
nostarch_url    = 'https://nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))

simple_url      = nostarch_url.removeprefix("https://")
print(simple_url)

# Apostrophe error with Single/Double quote #
message         = "One of the python's strength is its diverse community."
print(message)

message_error   = 'One of the pythons strength is its diverse community.'  # --> this is the error
print(message_error)






