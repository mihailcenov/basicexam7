# min and max capacity value
MIN_CAPACITY = 100.0
MAX_CAPACITY = 6000.0

# Input Plane capacity for luggage in [MIN_CAPACITY .. MAX_CAPACITY]
while True:
    capacity = float(input())
    if capacity >= MIN_CAPACITY and capacity <= MAX_CAPACITY:
        break

# print(f"Capacity = {capacity}")
luggage_counter = 0
# loop to to load luggage into the plane
while capacity > 0.0:
    command = input()
    if command == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break
    luggage_volume = float(command)
    # print(f"luggage_vol = {luggage_volume}")
    luggage_counter += 1
    if luggage_counter % 3 == 0:
        luggage_volume *= 1.10
    #print(f"{luggage_counter} {luggage_volume}")
    if capacity > luggage_volume:
        capacity -= luggage_volume
    else:
        luggage_counter -= 1
        print(f"No more space!")
        break

print(f"Statistic: {luggage_counter} suitcases loaded.")
