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

    #loop through each number
    #use counter to modify only green elements
    green_counter = 0
    for number in numbers:
        neg_number = int(number)
        neg_number = 255 - neg_number

            #otherwise, append normal number
        modified_line.append(str(neg_number))


    #turn list of numbers back into a string
    output = ' '.join(modified_line)

    #write to output file
    print(output, file=ppm_output)

#close files
ppm_input.close()
ppm_output.close()
