seats = 100
def book(n):
    global seats
    if n <= seats:
        seats = seats - n
        print("Booked", n, "seats. Remaining:", seats)
    else:
        print("Only", seats, "seats left. Booking failed.")
def cancel(n):
    global seats
    seats = seats + n
    print("Cancelled", n, "seats. Remaining:", seats)
def status():
    print(seats, "seats available out of 100")
book(3)
book(10)
book(200)
cancel(5)
status()