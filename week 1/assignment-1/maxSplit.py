S = input()
countR = 0
countL = 0
result = []
current_string = ""


for char in S:
    current_string += char
    if char == 'R':
        countR += 1
    else:
        countL += 1

    if countR == countL:
        result.append(current_string)
        current_string = ""

print(len(result))
for str in result:
    print(str)