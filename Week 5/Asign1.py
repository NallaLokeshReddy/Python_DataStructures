#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input('Enter the file name: ')
fhandle = open(fname)
reg_mailer = dict()      # regular mailer
for line in fhandle:
    if line.startswith('From') :
        if line[4] is ':' :
            continue
        else:
            words = line.split()
            mail = words[1]
    else:
        continue

    # reg_mailer[mail] = reg_mailer.get(mail,0) + 1

    if reg_mailer is None or mail not in reg_mailer :
        reg_mailer[mail] = 1
    else:
        reg_mailer[mail] = reg_mailer[mail] + 1

a = max(reg_mailer.values())
for key, value in reg_mailer.items() :
    if value == a :
        print(key,a)
    else:
        continue
