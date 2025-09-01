#!/usr/bin/env python3
import sys


# initialise state value
# go thorough the current key, count total number, sum of fare
# highest fare and lowest fare
current_key = None
trip_count = 0
total_fare = 0.0
max_fare = None
min_fare = None


# read each line from the mapper's output line by line
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    key, count_str, max_str, min_str, fare_str = line.split('\t')

    count = int(count_str)
    max_val = float(max_str)
    min_val = float(min_str)
    fare_sum = float(fare_str)
    
    
    # if reaching a new key, print the result for the previous group
    # print toal trip, max/min/avarage fare
    # reset the counters for the new group
    if key != current_key and current_key is not None:
        taxi_id, trip_type = current_key.split("_")
        # output previous key result
        avg_fare = total_fare / trip_count if trip_count else 0.0
        print(f"{taxi_id}\t{trip_type}\t{trip_count}\t{max_fare:.2f}\t{min_fare:.2f}\t{avg_fare:.2f}")

        # reset accumulator for new key
        trip_count = 0
        total_fare = 0.0
        max_fare = None
        min_fare = None
    # of it in the same group just adding number of trip , total fare, max and min

    current_key = key
    trip_count += count
    total_fare += fare_sum
    max_fare = max(max_fare, max_val) if max_fare is not None else max_val
    min_fare = min(min_fare, min_val) if min_fare is not None else min_val


# Output the last key after finshing the loop
if current_key:
    taxi_id, trip_type = current_key.split("_")
    avg_fare = total_fare / trip_count
    print(f"{taxi_id}\t{trip_type}\t{trip_count}\t{max_fare:.2f}\t{min_fare:.2f}\t{avg_fare:.2f}")