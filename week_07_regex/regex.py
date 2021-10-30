import re


def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern = r"(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    result = result + re.findall(pattern,line)
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

def find_name(line):
  pattern = r"(Mr|Ms|Mrs|Dr)\.?([\ ][A-Z][a-z]*)( [A-Z][a-z]*)?"
  result = re.findall(pattern,line)
  pattern = r"([A-Z][a-z]+)( [A-Z][a-z]*)"
  result2 = re.findall(pattern, line)
  result.extend(result2)
  
  print("Result: " + str(result))
  return result


f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)

'''
Grab the regex.py code from the class site. Modify it so that it reads
a text file and uses regexes to find as many names in the text file as
possible. For example "John Smith" would be a name as would "Mrs. Cho."
Remember that you will likely have to use multiple regular expressions
to handle different cases just like we did in class to identify dates.
Create or edit your text file so that it has data to read in and test
itself on.
When run, your program should print out all the names it finds. Don't
worry about formatting, you can just print the results of your calls
to re.findall() or any other calls you make.
'''
