flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100},
    "UK301": {"source": "Delhi", "dest": "Kolkata", "seats": 2, "price": 6000},
    "UK302": {"source": "Kolkata", "dest": "Delhi", "seats": 6, "price": 6200}
}

def flight_booking():
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    found = False

    for flight_no, details in flights.items():

        if details["source"].lower() == source.lower() and details["dest"].lower() == destination.lower():

            found = True

            print("\nFlight Available")
            print("Flight Number:", flight_no)
            print("Price:", details["price"])
            print("Available Seats:", details["seats"])

            seats = int(input("Enter number of seats: "))

            if seats <= details["seats"]:
                details["seats"] -= seats

                total_amount = seats * details["price"]

                print("\nBooking Successful")
                print("Seats Booked:", seats)
                print("Total Amount:", total_amount)
                print("Remaining Seats:", details["seats"])

            else:
                print("Sorry! Seats not available")

            break

    if not found:
        print("No Flight Found")

flight_booking()
