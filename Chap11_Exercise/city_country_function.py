def city_country_name(city, country, population = None):
    """Format the name to [city, country - population XXXX]"""
    if population:
        formatted_name  = f"{city}, {country} - population {population}"
    else:
        formatted_name  = f"{city}, {country}"
    return formatted_name
