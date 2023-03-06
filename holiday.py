# This function takes in the number of nights which is multiplied by the price per night and returns the total hotel cost
def hotel_cost(num_of_nights):
    price_per_night = 50
    return num_of_nights * price_per_night


# This function takes in the city the user is flying to and it returns the flight price
def plane_cost(city):
    if city == "London":
        flight_cost = 50
        return flight_cost
    elif city == "Rome":
        flight_cost = 60
        return flight_cost
    elif city == "Cape Town":
        flight_cost = 70
        return flight_cost


# This function takes in the number of days the user requires  a hire car, which is multiplied by the daily price and returns the total car rental cost
def car_rental(num_of_days):
    cost_per_day = 30
    return num_of_days * cost_per_day


# This function calculates and returns the total holiday cost by adding the hotel cot, the plane cost and the car rental
def holiday_cost(num_of_nights, city, num_of_days):
    total_holiday_cost = int(
        hotel_cost(num_of_nights) + plane_cost(city) + car_rental(num_of_days)
    )
    return total_holiday_cost


# User to input the number of nights of his hotel stay, the city he is flying to and the number of days for which he needs a hire car
num_of_nights = int(input("How many nights will you be staying at the hotel? "))
city = input("Which city are you flying to?(London, Rome or Cape Town) ").title()
num_of_days = int(input("How many days do you need to hire a car for? "))

# Output the details and total cost of the holiday
print(
    f"Your booking includes a flight to {city}, {num_of_nights} night stay at the hotel and a car rental for {num_of_days} days. The total cost of your booking is £",
    holiday_cost(num_of_nights, city, num_of_days),
)
