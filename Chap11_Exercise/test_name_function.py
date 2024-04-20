from name_function import get_formatted_name

def test_first_last_name():
    """Do name like John Joplin work?"""
    formatted_name      = get_formatted_name('John', 'Joplin')
    assert formatted_name   == 'John Joplin'

def test_first_middle_last_name():
    """Do name like John C Joplin work?"""
    formatted_name      = get_formatted_name('John', 'Joplin', 'C')
    assert formatted_name   == 'John C Joplin'