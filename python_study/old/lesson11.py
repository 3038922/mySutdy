# 集合
country = set(["china", "russia", "india"])
print("india" in country)
print("usa" in country)
countryCopy = country.copy()
countryCopy.add("usa")
country.remove("russia")
print(country & countryCopy)
