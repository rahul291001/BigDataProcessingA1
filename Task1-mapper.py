#!/usr/bin/env python3
import sys

dict = {}

# Input comes from standard input
for line in sys.stdin:
    line = line.strip()

    # break the line into column
    # split one line of text into multiple value using comma
    parts = line.split(",")

    # get the taxi_id, fare and distance stating from taxi id
    taxi_id = parts[1]
    fare = float(parts[2])
    distance = float(parts[3])

    # Determine trip type based on distance
    if distance >= 200:
        trip_type = "long"
    elif distance >= 100:
        trip_type = "medium"
    else:
        trip_type = "short"

    # combine taxi ID and trip type into a string 
    key = f"{taxi_id}_{trip_type}"

    # If key not in dictionary, initialize list: [count, total_fare, max_fare, min_fare]
    if key not in dict:
        dict[key] = [1, fare, fare, fare]
    else:
    # if the key has already existed, add 1 to trip count and add fare as well
    # also check the new fare in the exiting key
    # if it greater than previous one, update max
    # if it less than previous one, update min
        dict[key][0] += 1
        dict[key][1] += fare
        dict[key][2] = max(dict[key][2], fare)
        dict[key][3] = min(dict[key][3], fare)

# Emit key-value pairs from dictionary
# loop through every entry inside the dict
for key, value in dict.items():

    # splite the key into two parts
    # then pick the first part and second parrt of each key
    # then also extract total trip for fare, max fare and min fare

    # Output result with tab-separated fields
    count, total_fare, max_fare, min_fare = value
    print(f"{key}\t{count}\t{max_fare:.2f}\t{min_fare:.2f}\t{total_fare:.2f}")

