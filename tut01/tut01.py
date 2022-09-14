import csv
with open('octant_input.csv', 'r') as file:
    file = csv.reader(file)
    with open('new_octant.csv', 'w')as csv_file:
        csv_file = csv.writer(csv_file)
        for line in file:
            csv_file.writerow(line)
