#!/usr/bin/env bash
# Task 3 runner: Join (Job 1) -> Count (Job 2) -> Sort ascending by total trips (Job 3)

set -euo pipefail

JAR="./hadoop-streaming-3.1.4.jar"

# Sanity check for JAR
if [[ ! -f "$JAR" ]]; then
  echo "ERROR: $JAR not found in current directory." >&2
  exit 1
fi

# Clean intermediate and final outputs if they exist
hadoop fs -rm -r -f /Output/Task3_job1 >/dev/null 2>&1 || true
hadoop fs -rm -r -f /Output/Task3_job2 >/dev/null 2>&1 || true
hadoop fs -rm -r -f /Output/Task3     >/dev/null 2>&1 || true

# Job 1: Reduce-side join on Taxi# to attach company to each taxi's trips
hadoop jar "$JAR" \
  -D mapreduce.job.name="Task3-Job1-Join" \
  -D mapreduce.job.reduces=3 \
  -files task3_job1_mapper.py,task3_job1_reducer.py \
  -input /Input/Trips.txt \
  -input /Input/Taxis.txt \
  -output /Output/Task3_job1 \
  -mapper "python3 task3_job1_mapper.py" \
  -reducer "python3 task3_job1_reducer.py"

# Job 2: Sum counts per company
hadoop jar "$JAR" \
  -D mapreduce.job.name="Task3-Job2-Count" \
  -D mapreduce.job.reduces=3 \
  -files task3_job2_mapper.py,task3_job2_reducer.py \
  -input /Output/Task3_job1 \
  -output /Output/Task3_job2 \
  -mapper "python3 task3_job2_mapper.py" \
  -reducer "python3 task3_job2_reducer.py"

# Job 3: Sort ascending by total_count (numeric), then by company_id
hadoop jar "$JAR" \
  -D mapreduce.job.name="Task3-Job3-Sort" \
  -D mapreduce.job.reduces=3 \
  -D stream.map.output.field.separator=$'\t' \
  -D stream.num.map.output.key.fields=2 \
  -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2" \
  -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
  -files task3_job3_mapper.py,task3_job3_reducer.py \
  -input /Output/Task3_job2 \
  -output /Output/Task3 \
  -mapper "python3 task3_job3_mapper.py" \
  -reducer "python3 task3_job3_reducer.py"

echo "Task 3 completed. Final output at /Output/Task3"
