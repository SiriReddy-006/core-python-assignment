trips = [5,10,3]
def taxi_fare():
    total = 0
    for i, d in enumerate(trips, 1):
        f = 50 + d*10
        print("Trip", i, ":", f)
        total += f
    print("Total Fare:", total)

taxi_fare()
