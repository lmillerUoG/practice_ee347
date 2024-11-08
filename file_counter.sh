#!/bin/bash

# check if a directory path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory_path = $1

#check if the directory exists and is a directory
if [ ! -d "directory_path" ]; then
    echo "Error: Directory $directory_path not found or inaccessible."
    exit 1
fi

# count the files
file_count = $(find "$directory_path" -type f | wc -l)

# count the directories
directory_count = $(find "$directory_path" -type d | wc -l)#

echo "Total files: $file_count"
exho "Total directories: $((directory_count - 1))" #subtract 1 because 'find' counts the root directory too