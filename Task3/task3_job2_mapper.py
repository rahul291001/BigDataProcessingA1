
#!/usr/bin/env python3
# Mapper for Job 2: Counting trips per company.
# Input: "<company_id>\t<trip_count_for_this_taxi>"
# Output: "<company_id>\t<trip_count_for_this_taxi>"
# (identity mapper; kept explicit for clarity and future tweaks)
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
    company_id, cnt = parts
    # validate numeric-ish
    try:
        int(company_id)
        int(cnt)
    except Exception:
        continue
    print(f"{company_id}\t{cnt}")
