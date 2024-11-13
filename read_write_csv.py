import csv

students = []
total_score = 0

with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)    #skip header row
    
    # loop through each row in csv file
    for row in reader:
        name = row[0]   # get student's name from first column
        score = int(row[1])     # converge score to an integer

        # append (name, score) tuple to students list
        students.append((name, score))

        # add score to total_score for calculating the avg later
        total_score += score

# calculate avg score
avg_score = total_score / len(students)

# determin pass/fail
results = []    #list to store name, score, pass/fail status

for name, score in students:
    #determine pass/fail
    status = "Pass" if score >= avg_score else "Fail"

    results.append((name, score, status))

#write data to students_results.csv
with open('students_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)        # create a csv writer object

    # write the header row to csv file
    writer.writerow(['Name', 'Score', 'Status'])

    # write each students result to csv file
    writer.writerows(results)
