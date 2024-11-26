# Open the source file in read mode and the destination file in write mode
with open('emails.csv', 'r') as source_file, open('output.csv', 'w') as destination_file:
    # Read each line from the source file
    for line in source_file:
        new_line = "," + line.strip() + ",,,,,\n"
        destination_file.write(new_line)
    