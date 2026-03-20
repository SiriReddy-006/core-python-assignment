total_seats = 10
booked = [2, 5, 7]

def book():
    s = int(input("Enter seat number to book: "))
    if s in booked:
        print("Seat already booked")
    elif s < 1 or s > total_seats:
        print("Invalid seat number")
    else:
        booked.append(s)
        print("Seat booked successfully")

def cancel():
    s = int(input("Enter seat number to cancel: "))
    if s in booked:
        booked.remove(s)
        print("Seat cancelled")
    else:
        print("Seat was not booked")

def show_available():
    available = []

    for seat in range(1, total_seats + 1):
        if seat not in booked:
            available.append(seat)

    print("Available seats:", available)

def show_booked():
    print("Booked seats:", booked)
  
def main():
    while True:
        print("\n---- Movie Booking System ----")
        print("1. Book seat")
        print("2. Cancel seat")
        print("3. Show available seats")
        print("4. Show booked seats")
        print("5. Exit")

        choice = int(input("Choose option: "))
        if choice == 1:
            book()
        elif choice == 2:
            cancel()
        elif choice == 3:
            show_available()
        elif choice == 4:
            show_booked()
        elif choice == 5:
            print("Exiting program")
            break
        else:
            print("Invalid choice")
          
main()
