"""HomeTask_9.

write script that will read "input.txt" file and find there all characters from english alphabet
collect these characters and their positions in file
after info collected this info as text write to "output.txt" file in such format
####################
<first found letter> -> pos1
<next_letter> -> pos2
<next_letter -> pos3
etc
#######################
"""
import re

with open('input.txt', 'r') as inp:  # open the file for reading
    data = inp.read()
    regexp = re.finditer(r'[a-zA-Z]', data)  # find the all characters from english alphabet
    d1 = {i.group(): i.start() for i in regexp}  # collect these characters and their positions in file
output = ""  # prepare the string of letters and positions
for key, value in d1.items():
    output += f"{key} -> {value}\n"

    with open('output.txt', 'w') as out:  # open the file for writing of the prepared string
        out.write(output)
print(output)




