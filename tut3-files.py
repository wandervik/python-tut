# file_min = open('test_min.js', 'w')

with open('test.js') as file:
    with open('test_min.js', 'w') as file_min:
        for line in file:
            if not line.isspace():
                file_min.write(line)



    # content = file.read()
    # print(content)






# file = open('test.txt')
# content = file.read()
# print(content)

# file.seek(0)
# content2 = file.read()
# # print(f'content2: {content2}')
# print('content2:\n' + content2)

