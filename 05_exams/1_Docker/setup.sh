#!/bin/bash


mkdir -p logs

#buld the image
docker build -t exam_tests .   # dont forget the "."

# start composition
docker compose down
docker compose up --abort-on-container-exit  # stops here when container are while runnung

# copy logs if they exist AND LOG=1
if [ -f logs/api_test.log ]; then
    cp logs/api_test.log log.txt
else
    echo "WARN: logs/api_test.log not found"
fi

echo "Done, Results in log.txt"