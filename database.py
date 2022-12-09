import csv

# Open the file in write mode
with open("file.txt", "w") as f:
    # Write some text to the file
    f.write("Hello, world!")

# Open the file in append mode
with open("file.txt", "a") as f:
    # Append more text to the file
    f.write("\nThis is a new line.")

# Open the file in read mode
with open("file.txt", "r") as f:
    # Read the contents of the file
    print(f.read())  # Should print "Hello, world!\nThis is a new line."


dic = {}
with open('hw5q7.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(row)
            rows = []
            row[0].replace("\\", " ")
            rows = row[0].split()
            #print(rows)
            total_cost = int(rows[2]) * int(rows[3])
            print(f'\t Customer number {rows[0]} purchased {rows[3]} {rows[1]} for  {rows[2]} each, giving a total cost of ${total_cost} dollars.')
            try:
                if dic[rows[0]]:
                    dic[rows[0]] += total_cost
            except:
                dic[rows[0]] = total_cost    
            line_count += 1
    #print(f'Processed {line_count} lines.')
for i in dic:
    print(f'\t Customer number {i} had a total bill of ${dic[i]}')
