
#!/usr/bin/env python3
# Reducer for Job 3:
# Input key: "<total_count>\t<company_id>" (sorted by count asc, then company)
# Output: "<company_id>\t<total_count>"
# Reducer simply reverses key order and emits final result in required format.
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) < 2:
        continue
    # Allow extra tabs (defensive); last two fields are count and company
    count_s, company_id = parts[0], parts[1]
    # Validate integer-ish
    try:
        int(count_s)
        int(company_id)
    except Exception:
        continue
    print(f"{company_id}\t{count_s}")
