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
    regexp = re.findall(r'[a-zA-Z]', data)  # find the all characters from english alphabet
    with open('output.txt', 'w') as out:  # open the file for writing
        for i in regexp:  # collect these characters and their positions in file
            out.write(f'{i} -> pos{regexp.index(i) + 1}\n')
    with open('output.txt', 'r') as out: # open the file for reading
        output_text = out.read()
print(output_text)


