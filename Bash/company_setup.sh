#!/bin/bash


## SCRIPT SETUP ##

# get the base directory name where file/folders will be created from the user
echo "Enter the base directory name:"
read BASE_DIR
# define the log file path inside the base directory
LOG_FILE="${BASE_DIR}/creation_log.txt"

# create the base directory
mkdir -p "$BASE_DIR" || exit 1     # exit if directory change fails

# function to log actions with a timestamp, adding entries to the log file
log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}



## STRUCTURE SETUP ##

# create Departments folder with three department subfolders: HR, IT, Sales
mkdir -p "$BASE_DIR/Departments/HR" "$BASE_DIR/Departments/IT" "$BASE_DIR/Departments/Sales"

# set permissions on Departments folder to user-only access (read, write, execute)
chmod 700 "BASE_DIR/Departments"

# create employees folder with two subfolders: Active and Inactive
mkdir -p "$BASE_DIR/Employees/Active" "$BASE_DIR/Employees/Inactive"

# set permissions for Employees folder to user and group read/write only (no execute)
chmod 660 "$BASE_DIR/Employees"




## FILE CREATION IN DEPARTMENTS ##

# Create dept_info.txt in each department
for dept in Departments/*; do
    echo "This is the ${dept##*/} department." > "$dept/dept_info.txt"
    log_action "Created dept_info.txt in ${dept}."
done



## ADD EMPLOYEE MANAGEMENT FEATURE ##

# get employee name and status
echo "Enter employee name:"
read EMPLOYEE_NAME
echo "Enter employee status (active/inactive):"
read STATUS

# create employee file in the correct folder
if [[ "$STATUS" == "active" ]]; then
    echo "$EMPLOYEE_NAME" > "$BASE_DIR/Employees/Active/$EMPLOYEE_NAME.txt"
    log_action "Added employee $EMPLOYEE_NAME to Active."
else
    echo "$EMPLOYEE_NAME" > "$BASE_DIR/Employees/Inactive/$EMPLOYEE_NAME.txt"
    log_action "Added employee $EMPLOYEE_NAME to Inactive."
fi



## ADVANCED SEARCH FEATURE WITH COMMENTS ##

# prompt the user for a search term to find in the base directory
echo "Enter search term:"
read SEARCH_TERM

echo "Searching for '$SEARCH_TERM' in $BASE_DIR..."
grep -rnw "$BASE_DIR" -e "$SEARCH_TERM" | while read -r line; do
    echo "$line"
    log_action "Search term '$SEARCH_TERM' found: $line"
done