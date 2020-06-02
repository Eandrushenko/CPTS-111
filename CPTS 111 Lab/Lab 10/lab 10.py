input_file_name = input("Enter a ppm file: ")
output_file_name = input("Enter an output file: ")
counter = 0

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

file_contents = input_file.readlines()

for line in file_contents:
        line = line.strip()
        numbers = line.split(" ")
        counter += 1
        if counter > 3:
                for i in range(1,len(numbers),3):
                        numbers[i] = '0'
                        
                text = " ".join(numbers)
                print(text, file=output_file)
        else:
                print(line, file=output_file)

        

input_file.close()
output_file.close()
