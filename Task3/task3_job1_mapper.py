
#!/usr/bin/env python3
# Mapper for Job 1: Reduce-side join Trips (by Taxi#) with Taxis to get company per Taxi.
# Emits: key = TaxiID, value = tagged payload
#   For Taxis.txt rows:     "TAX\t<company_id>"
#   For Trips.txt rows:     "TRIP"
# The reducer will count trips per TaxiID and output: "<company_id>\t<trip_count_for_this_taxi>"
import sys

def is_header(fields):
    if not fields:
        return True
    f0 = fields[0].strip().lower()
    return f0 in ("trip#", "taxi#")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = [p.strip() for p in line.split(",")]
    # Skip header lines from either file
    if is_header(parts):
        continue

    # Identify source by number of fields:
    # Taxis.txt: 4 fields => Taxi#, company, model, year
    # Trips.txt: 8 fields => Trip#, Taxi#, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y
    try:
        if len(parts) == 4:
            taxi_id = parts[0]
            company_id = parts[1]
            # Validate numeric taxi_id
            int(taxi_id)
            print(f"{taxi_id}\tTAX\t{company_id}")
        elif len(parts) == 8:
            taxi_id = parts[1]
            # Validate numeric taxi_id
            int(taxi_id)
            print(f"{taxi_id}\tTRIP")
        else:
            # Unrecognized row; silently skip (robustness)
            continue
    except Exception:
        # Skip malformed rows
        continue
