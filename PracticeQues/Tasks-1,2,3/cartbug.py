def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))