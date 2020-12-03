a_file = open("C2asciiwgetzz.txt")

new_list = []
lines = a_file.readlines()
for line in lines:
    new_list.append(line)
    
#for row in new_list:
    #print(row)

b = len(new_list)

import os
lists = []
for filename in os.listdir("/Volumes/ExtremeSSD/c2txt"):
    lists.append(filename)
    
a = len(lists)
to_go = b - a
print(to_go)
