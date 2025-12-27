import re
# inp = input("enter it like normal no fancy inputs needed:")
inp = "*T+12 + 3 *   4 - 2salam / 1 ^-+ 2 %   3 2/"              #test input


def calc(x):
    refine = re.sub(r"[^\d+\-*/%^]" , "" , inp)                     #removes whitespaces and letters
    refine = re.sub(r"(?<=[+\-*/%^])[+\-*/%^]+" , "" , refine)      #removes duplicate operators and only keeps the first one
    # print(refine)

    numbers = re.findall(r"\d+" , refine)
    # print(numbers)

    oprations = re.findall(r"(?<=\d)[+\-*/%^](?=\d)" , refine)
    # print(oprations)

    numbers = [int(x) for x in numbers]
    for index , op in enumerate(oprations):
        if op == "^":
            numbers[index] = numbers[index] ** numbers[index + 1]
            del numbers[index + 1]
            del oprations[index]

    for index , op in enumerate(oprations):
        if op == "*":
            numbers[index] = numbers[index] * numbers[index + 1]
            del numbers[index + 1]
            del oprations[index]

    for index , op in enumerate(oprations):
        if op == "/":
            numbers[index] = numbers[index] / numbers[index + 1]
            del numbers[index + 1]
            del oprations[index]

    for index , op in enumerate(oprations):
        if op == "%":
            numbers[index] = numbers[index] % numbers[index + 1]
            del numbers[index + 1]
            del oprations[index]

    for index , op in enumerate(oprations):
        if op == "+":
            numbers[index] = numbers[index] + numbers[index + 1]
            del numbers[index + 1]
            del oprations[index]

    for index , op in enumerate(oprations):
        if op == "-":
            numbers[index] = numbers[index] - numbers[index + 1]
            del numbers[index + 1]
            del oprations[index]

    return numbers[0]

print("javab:" , calc(inp))
print(12+3*4-2/1**2%32)

while True:
    inp = input("equation:")
    print("javab:" , calc(inp))
    print("done")