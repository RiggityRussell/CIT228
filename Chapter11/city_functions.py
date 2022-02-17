#Russell Arlt
#Hands on #1

print("-----------------------Exercise 11-1-----------------------")
def cityCountry(cityName, countryName, pop=""):
    if pop:
        names = (f"{countryName.title()}, {cityName.title()}, Population: {pop}")
        return names
    else:
        names = (f"{countryName.title()}, {cityName.title()}")
        return names
