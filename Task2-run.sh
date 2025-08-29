
JAR=hadoop-streaming-3.1.4.jar
INPUT=Trips.txt
OUTPUT=/Output/Task2


cp initialization.txt current_medoids.txt


ITER=$(head -n 1 initialization.txt)

for ((i=1; i<=ITER; i++))
do
    echo "Iteration $i"

   
    hadoop fs -rm -r -f $OUTPUT


    hadoop jar $JAR \
        -D mapreduce.job.reduces=3 \
        -input $INPUT \
        -output $OUTPUT \
        -mapper "python3 Task2-mapper.py" \
        -reducer "python3 Task2-reducer.py" \
        -file Task2-mapper.py \
        -file Task2-reducer.py \
        -file current_medoids.txt


    hadoop fs -getmerge $OUTPUT new_medoids.txt

   
    echo "After iteration $i:"
    cat new_medoids.txt

 
    if cmp -s new_medoids.txt current_medoids.txt; then
        echo "Converged at iteration $i"
        break
    fi

    
    cp new_medoids.txt current_medoids.txt
done


cp new_medoids.txt Task2_output.txt
echo "Final medoids written to Task2_output.txt"
