#!/usr/bin/bash

echo "Stopping uvicorn process ..."

uvicornProc=($(lsof -iTCP -MnP | grep LISTEN | grep ":8000 (LISTEN)" | awk '{print $2}'))
for procId in "${uvicornProc[@]}"
do
    if [[ $procId != "1" ]]; then
        kill -9 $procId
        echo "Killing previous process $procId ..."
    fi
done