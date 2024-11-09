ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

num_flavors: int = len(ice_cream)
print(str(num_flavors) + " flavors")

ice_cream["vanilla"] += 10

ice_cream.pop("strawberry")

for flavor in ice_cream:
    print("We have " + flavor + " ice cream.")

print(ice_cream)
