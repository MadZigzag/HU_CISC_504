DEFAULT_INITIAL_BASKET = ["orange", "apple"]

def create_picnic_basket(healthy, hungry, initial_basket=DEFAULT_INITIAL_BASKET):
    basket = initial_basket
    if healthy:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket

# Reproducer

def create_picnic_basket(healthy, hungry, initial_basket = None):
    if initial_basket is None:
        initial_basket = ["orange", "apple"]
    basket = initial_basket
    if healthy:
        basket.append("strawberry")
    else:
        basket.append("jam")

    if hungry:
        basket.append("sandwich")
    return basket
print("First basket:", create_picnic_basket(True, False))
print("Second basket:", create_picnic_basket(False, True, ["tea"]))
print("Third basket:", create_picnic_basket(True, True))

print("WHY DO I HAVE 2 STRAWBERRIES WHEN I AM HEALTH AND HUNGRY?")