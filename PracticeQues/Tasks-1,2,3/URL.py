def build_query(**filters):
    result = ""
    for key, value in filters.items():
        if result != "":
            result = result + "&"
        result = result + key + "=" + str(value)
    return result
print(build_query(city="hyderabad", rating=4, veg=True))
print(build_query())