#!/bin/bash

# get the process name from the first argument
process_name=$1

# check if user provided a process name
if [ -z "$process_name" ]; then
    echo "Usage: $0 process_name"
    exit 1
fi

# check if the process is running using pgrep
if pgrep -x "$process_name" > /dev/null; then
    echo "$process_name is running."
else
    echo "$process_name is not running."
fi