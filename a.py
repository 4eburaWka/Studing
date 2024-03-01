import csv


string = '''1 124000 33,3333 41333,3333 50 62000 124000 83,3 103292
2 124000 33,3333 41333,3333 33 40920 20708 83,3 17249,764
3 124000 33,3333 41333,3333 17 21080 3458,236 83,3 3458,236'''

arr = [s.split() for s in string.split('\n')]
print(*arr, sep='\n')

csv_file_path = 'matrix.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in arr:
        csv_writer.writerow(row)