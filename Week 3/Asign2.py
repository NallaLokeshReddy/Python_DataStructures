#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# when you are testing below enter mbox-short.txt as the file name.

fname = input('Enter the file name: ')
fhandle = open(fname)
count = 0
Total = 0
for line in fhandle :
    if 'X-DSPAM-Confidence:' in line :
        Colpos = line.find(':')
        num_string = line[Colpos + 1 : ]
        num = float(num_string)
        count = count + 1
        Total = Total + num
    else:
        continue

avg = Total / count
print('Average spam confidence:',avg)
