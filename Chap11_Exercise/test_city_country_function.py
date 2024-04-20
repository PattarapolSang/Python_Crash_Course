from city_country_function import city_country_name

def test_city_country_function():
    name    = city_country_name("Bangkok", "Thailand")
    assert  name == 'Bangkok, Thailand'

def test_population():
    name    = city_country_name("Bangkok", "Thailand", 50000)
    assert  name == 'Bangkok, Thailand - population 50000'