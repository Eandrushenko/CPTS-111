#Ask user for a file to read
txt_file = input("Enter a file name: ")

#Read the file
print("Reading", txt_file)
num_file = open(txt_file, 'r')

lines = num_file.readlines()
num_file.close()
num_numbers = 0
numbers_total = 0
num_chars = 0
num_words = 0
largest_number = 0
smallest_number = 100000
largest_word = " "
smallest_word = "abc..................."

for line in lines:
    line = line.strip()
    is_word = True

    

    
    
