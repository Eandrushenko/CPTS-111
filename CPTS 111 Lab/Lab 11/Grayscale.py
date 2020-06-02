print("Remove green from PPM:")
ppm_file_name = input("Enter a PPM file to parse: ")
ppm_destination = input("Enter destination file: ")
print("parsing...")

ppm_input = open(ppm_file_name, 'r')
ppm_output = open(ppm_destination, 'w')

#copy over first three lines into destination file
line = ppm_input.readline()
print(line, file=ppm_output, end="")
line = ppm_input.readline()
print(line, file=ppm_output, end="")
line = ppm_input.readline()
print(line, file=ppm_output, end="")

#now, work through each line in the file
file_contents = ppm_input.readlines()
for line in file_contents:

    #split line based on spaces
    numbers = line.strip().split(' ')

    #contains our modified numerical values
    modified_line = list()

    for i in range(0, len(numbers), 3):

        red_start = int(numbers[i])
        green_start = int(numbers[i + 1])
        blue_start = int(numbers[i + 2])

        average_value = (red_start + green_start + blue_start) // 3

        for j in range(3):
            
            #note: this must be a string!
            modified_line.append(str(average_value))


        

    #turn list of numbers back into a string
    output = ' '.join(modified_line)

    #write to output file
    print(output, file=ppm_output)

#close files
ppm_input.close()
ppm_output.close()
