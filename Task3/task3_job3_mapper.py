
#!/usr/bin/env python3
# Mapper for Job 3: Sorting by total trips (ascending).
# Input: "<company_id>\t<total_count>"
# Output key: "<total_count>\t<company_id>"
# Using a numeric comparator (-k1,1n -k2,2) in the run script to sort by count asc, then company.
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
    company_id, total_s = parts
    try:
        int(company_id)
        # Keep count as-is; comparator will handle numeric sort
        int(total_s)
    except Exception:
        continue
    print(f"{total_s}\t{company_id}")
