# TASK1_numbers
def water_calculation(r, pi=3.14, square_meter=1.4):
    pond_area = pi * (r ** 2)
    total_water = int(pond_area * square_meter)  # Casting to int to remove decimals
    return pond_area, total_water
def speed_calculation(distance, tm):
    ts = tm * 60
    speed = int(distance / ts)
    return speed

radius = 84
area, water = water_calculation(radius)

distance = 490
tm = 7
speed = speed_calculation(distance, tm)


print("Pond Area: {:.2f} sq meters".format(area))
print("Total Water: {} liters".format(water))
print("Speed: {} m/s".format(speed))