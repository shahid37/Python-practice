cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("there are " + str(cars) + " cars available")
print("there are only " + str(drivers) + " drivers available")
print("there will be " + str(cars_not_driven) + " empty cars today")
print("we can transport " + str(carpool_capacity) + " people today")
print("we have " + str(passengers) + " to carpool today")
print("we need to put about " + str(average_passengers_per_car) + " in each car")
