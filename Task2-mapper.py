#!/usr/bin/env python3
import sys
import math


centers = []
with open("current_medoids.txt") as file:
    for entry in file:
        vals = entry.strip().split()
        if len(vals) != 2:
            continue
        cx, cy = map(float, vals)
        centers.append((cx, cy))

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


for row in sys.stdin:
    fields = row.strip().split(",")
    if len(fields) < 8:
        continue
    dx, dy = float(fields[6]), float(fields[7])

 
    closest_idx, closest_val = 0, distance((dx, dy), centers[0])
    for idx, c in enumerate(centers[1:], start=1):
        d = distance((dx, dy), c)
        if d < closest_val:
            closest_idx, closest_val = idx, d

    print(f"{closest_idx}\t{dx},{dy}")
