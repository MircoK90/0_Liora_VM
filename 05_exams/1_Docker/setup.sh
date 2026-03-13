#!/bin/bash


mkdir -p logs

#buld the image
docker build -t exam_tests .   # dont forget the "."

# start composition
docker compose down     # for runtrough shut everything down before
docker compose up --abort-on-container-exit  # stops here when container are while runnung

# central log.txt file and Runnrtrough test after contr+c
if [ -f logs/api_test.log ]; then
    cp logs/api_test.log log.log
    echo "Done, Results in log.log"
else
    echo "WARN: logs/api_test.log not found"
fi

