#!/bin/bash

# check if the file path is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <filepath> [LOG_LEVEL]"
    exit 1
fi

file_path=$1
log_level=${2:-} #assign 2nd arg or leave empty if no 2nd arg

# check if the specified file exists and is readable
if [ ! -f "$file_path" ]; then
    echo "Error: File $file_path does not exist or is not accessible."
    exit 1
fi

# filter the log file based on the log level
if [ -z "$log_level" ]; then
    # no log level specified, display all entries
    cat "$file_path"
else
    # display only the specified log level entries
    grep "\[$log_level\]" "$file_path"
fi