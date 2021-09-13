# Lyuba Fridman
# Demonstrates dictionaries, loops
# Assignment: Create one or more Python programs in your week_01_python folder that exhibit your knowledge of Python including functions, lists and dictionaries.
# Write a program that reads a file and uses a dictionary to count the number of times each word appears.
all_words = {};
with open('book.txt') as f:
  line = f.readline()
  while line:
    words = line.split()
    for word in words:
      if word in all_words:
        all_words[word]+=1
      else:
        all_words[word] = 1  
    line = f.readline()
    #print(line)

print(all_words)