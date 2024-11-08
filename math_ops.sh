#!/bin/bash

#check if two args are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 num1 num2"
    exit 1
fi

echo "$1 + $2 = $(($1 + $2))"

echo "$1 - $2 = $(($1 - $2))"

echo "$1 * $2 = $(($1 * $2))"

if [ "$2" -ne 0 ]; then
    echo "$1 / $2 = $(($1 / $2))"
else
    echo "Division by zero is undefined."
fi

if [ "$2" -ne 0 ]; then
    echo "$1 % $2 = $(($1 % $2))"
else
    echo "Modulus by zero is undefined."
fi

echo "$1 ^ $2 = $(($1 ** $2))"