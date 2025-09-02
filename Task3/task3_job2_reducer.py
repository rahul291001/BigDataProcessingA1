
#!/usr/bin/env python3
# Reducer for Job 2: Sum counts per company.
# Input: "<company_id>\t<count_part>"
# Output: "<company_id>\t<total_count>"
import sys

current_company = None
total = 0

def flush():
    global current_company, total
    if current_company is not None:
        print(f"{current_company}\t{total}")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
    company, cnt_s = parts
    try:
        cnt = int(cnt_s)
    except Exception:
        continue

    if current_company is None:
        current_company = company

    if company != current_company:
        flush()
        current_company = company
        total = 0

    total += cnt

flush()
