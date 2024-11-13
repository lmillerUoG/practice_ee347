#!/bin/bash

# ensure PID is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <process_id>"
    exit 1
fi

process_id=$1

# loop until the process is no longe running
while kill -0 $process_id 2>/dev/null; do
    # kill -0 checks if the process exists without terminating it
    echo "Process $process_id is still running."
    sleep 5     # wait 5 secs before checking again
done

echo "Process $process_id has stopped"