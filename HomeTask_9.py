import re
with open('input.txt', 'r') as inp:
    data = inp.read()
    regexp = re.findall(r'[a-zA-Z]', data)
    with open('output.txt', 'w') as out:
        for i in regexp:
            out.write(f'{i} -> pos{regexp.index(i) + 1}\n')
    with open('output.txt', 'r') as out:
        output_text = out.read()
print(output_text)
# _____________________

