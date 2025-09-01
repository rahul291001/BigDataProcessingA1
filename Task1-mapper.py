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
    key = taxi_id + "_" + trip_type

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
        if fare > dict[key][2]:
            dict[key][2] = fare
        if fare < dict[key][3]:
            dict[key][3] = fare

# Emit key-value pairs from dictionary
# loop through every entry inside the dict
for key in dict:

    # splite the key into two parts
    # then pick the first part and second parrt of each key
    # then also extract total trip for fare, max fare and min fare
    taxi_trip = key.split("_")
    taxi_id = taxi_trip[0]
    trip_type = taxi_trip[1]
    total_trips = dict[key][0]
    total_fare = dict[key][1]
    max_fare = dict[key][2]
    min_fare = dict[key][3]
    avg_fare = total_fare / total_trips

    # Output result with tab-separated fields
    print('%s\t%d\t%.2f\t%.2f\t%.2f' % (key, total_trips, max_fare, min_fare, total_fare))

