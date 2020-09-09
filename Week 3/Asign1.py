# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# when you are testing below enter words.txt as the file name.

file = input('Enter the file name: ')
fhandle = open(file)
for line in fhandle:
    line_strip = line.strip()
    line = line_strip.upper()
    print(line)
