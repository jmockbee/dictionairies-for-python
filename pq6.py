def combine_guests(guests1, guests2):
    new_list = ""
    guests2.update(guests1)
    for key, value in guests2.items():
        if key in guests1:
            new_list = value + 1
            guests2[key] = new_list
        return guests2


# Combine both dictionaries into one, with each key listed
# only once, and the value from guests1 taking precedence

Rorys_guests = {
    "Adam": 2,
    "Brenda": 3,
    "David": 1,
    "Jose": 3,
    "Charlotte": 2,
    "Terry": 1,
    "Robert": 4,
}
Taylors_guests = {
    "David": 4,
    "Nancy": 1,
    "Robert": 2,
    "Adam": 1,
    "Samantha": 3,
    "Chris": 5,
}

print(combine_guests(Rorys_guests, Taylors_guests))
