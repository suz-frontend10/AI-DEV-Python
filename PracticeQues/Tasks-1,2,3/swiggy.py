def place_order(customer, *items, **charges):

    print("Customer :", customer)
    print("Items ordered ({}):".format(len(items)))
    for i in range(len(items)):
        print(" ", i + 1, ".", items[i])

    print("Charges:")
    for name, amount in charges.items():
        print(" ", name, ":", amount)

place_order("Ravi", "Biryani", "Coke", "Gulab Jamun",
            delivery=40, gst=25, discount=50)