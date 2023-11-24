with open('example.txt', 'w') as file:
    file.write('Hello, World!')

with open('example.txt', 'r') as file:
    content = file.read()
    print('Content of the file:', content)

with open('example.txt', 'a') as file:
    file.write('\nAppended text')

with open('example.txt', 'r') as file:
    updated_content = file.read()
    print('Updated content of the file:', updated_content)
