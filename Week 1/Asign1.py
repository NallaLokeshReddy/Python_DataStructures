#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence:    0.8475"
Colpos = text.find(':')       # Colon Position
text_a_Colpos = text[Colpos+1 : ]    # Text after colon position
number = text_a_Colpos.strip()
print(float(number))
ans = float(text_a_Colpos)
print(ans)

# Using Split and join functions
num_str = text_a_Colpos.split() # string format of number in list
d = ""
num = d.join(num_str)      # converts list into string
print(num)
num_f = float(num)
print(num_f)
# d = float(c)
# print(d)
