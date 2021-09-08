wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for key, value in wardrobe.items():
    for x in value:
        print("{} {}".format(x, key))
