#Ask user for a file to read
txt_file = input("Enter a file name: ")

#Read the file
print("Reading", txt_file)
num_file = open(txt_file, 'r')

lines = num_file.readlines()
num_file.close()
smallest_number = 1000000000000000000000000000000000000000000
largest_number = 0
number_count = 0
total_sum = 0
current_number = 0

for line in lines:
    line = line.strip()
    current_line = int(line)
    total_sum += current_line
    number_count += 1
    if current_line >= largest_number:
        largest_number = current_line
    if current_line <= smallest_number:
        smallest_number = current_line
    
print("Found",number_count,"numbers.")
avg = (total_sum / number_count)
print("Average: ", avg)
print("Largest number: ",largest_number)
print("Smallest number: ",smallest_number)
    
    
