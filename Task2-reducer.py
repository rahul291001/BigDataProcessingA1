#!/usr/bin/env python3
import sys
import math

def dist(a, b):
    """Euclidean distance"""
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

cluster_key = None
cluster_points = []

def emit_best(points):
    """Pick the medoid (point minimizing total distance)"""
    candidate = min(points, key=lambda pt: sum(dist(pt, other) for other in points))
    print(f"{candidate[0]}\t{candidate[1]}")

for row in sys.stdin:
    group, coords = row.strip().split("\t")
    px, py = map(float, coords.split(","))
    if cluster_key is None:
        cluster_key = group
    if group != cluster_key:
        emit_best(cluster_points)
        cluster_points = []
        cluster_key = group
    cluster_points.append((px, py))

if cluster_points:
    emit_best(cluster_points)
