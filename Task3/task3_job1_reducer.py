
#!/usr/bin/env python3
# Reducer for Job 1:
# Input (grouped by TaxiID): values tagged as "TAX\t<company_id>" and/or "TRIP"
# Output: "<company_id>\t<trip_count_for_this_taxi>"
# Notes:
# - We do NOT store all trips; we stream-count per TaxiID and emit one aggregated record per Taxi.
# - If a TaxiID has no company record, we drop its trips (outer-join not required by spec).

import sys

current_taxi = None
company_id = None
trip_count = 0

def flush():
    global current_taxi, company_id, trip_count
    if current_taxi is None:
        return
    if company_id is not None and trip_count > 0:
        print(f"{company_id}\t{trip_count}")
    # reset for next key
    company_id = None
    trip_count = 0

for line in sys.stdin:
    line = line.rstrip("\n")
    if not line:
        continue
    # Expect formats:
    # "<taxi>\tTAX\t<company>"
    # "<taxi>\tTRIP"
    parts = line.split("\t")
    if len(parts) < 2:
        continue
    taxi = parts[0]

    if current_taxi is None:
        current_taxi = taxi

    if taxi != current_taxi:
        flush()
        current_taxi = taxi

    tag = parts[1]
    if tag == "TAX":
        if len(parts) >= 3:
            company_id = parts[2]
    elif tag == "TRIP":
        trip_count += 1
    else:
        # unknown tag; ignore
        pass

# Flush last key
flush()
