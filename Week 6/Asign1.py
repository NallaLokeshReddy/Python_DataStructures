#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter the file name: ')
fhandle = open(fname)
time_mail = dict()
for line in fhandle:
    if line.startswith('From') :
        if line[4] is ':' :
            continue
        else:
            words = line.split()
            time = words[5]
            time_tup = time.split(':')
            time_tuple = time_tup[0]
    else:
        continue

    time_mail[time_tuple] = time_mail.get(time_tuple,0) + 1

    # if reg_mailer is None or mail not in reg_mailer :
    #     reg_mailer[mail] = 1
    # else:
    #     reg_mailer[mail] = reg_mailer[mail] + 1

ans = sorted(time_mail.items())
for k,v in ans:
    print(k,v)
