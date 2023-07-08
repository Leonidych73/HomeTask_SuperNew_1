import re
with open('input.txt', 'r') as inp:
    data = inp.read()
    regexp = re.findall(r'(?<![A-Z]{4})(?<=[A-Z]{3})[a-z](?<![A-Z])(?=[A-Z]{3})(?![A-Z]{4})', data)
    with open('output.txt', 'w') as out:
        for i in regexp:
            out.write(f'{i}')
    with open('output.txt', 'r') as out:
        output_text = out.read()
print(f'Result = "{output_text}"')
