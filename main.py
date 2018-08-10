import timeit
import csv
with open('dataset.csv') as csv_file:
    start = timeit.default_timer()
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tThe GameID {row[0]} is on Season {row[12]}.')
            line_count += 1
    stop = timeit.default_timer()
    print(f'Processed {line_count} lines in {stop - start } seconds.')
