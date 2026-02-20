import regex as re
# inp = input("enter it the way you like to enter it no fancy inputs needed:")
inp = "*T+12 + 3 *   ((4 - 2salam / 1 ^-+ 2 % ) +  (3 2))/"              #test input

def refine(x):
    refine = re.sub(r"[^\d+\-*/%^()]" , "" , x)                     #removes whitespaces and letters
    refine = re.sub(r"(?<=[+\-*/%^])[+\-*/%^]+" , "" , refine)      #removes duplicate operators and only keeps the first one
    print(refine)
    return refine
    
paratesis = re.compile(r"""
                        (?P<para>   
                            [([{]      #opeinig
                            (?:
                                [^()[\]{}]+  
                                |               #so if there is multiple parentheses it will not get bugged down
                                (?&para)        #recursion
                            )*
                            [)\]}]     #closing
                        )
                        """, re.VERBOSE)

paras = re.findall(paratesis , refine(inp)) 
print(paras)



def calc(x):
    refined = refine(x)
    # print(refine)

    numbers = re.findall(r"\d+" , refined)
    # print(numbers)

    oprations = re.findall(r"(?<=\d)[+\-*/%^](?=\d)" , refined)
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

print("javab:" , calc(inp))         #for showcase
print(12+3*4-2/1**2%32)             #its the inp aquation with normal python also for showcase

while True:
    inp = input("equation:")
    print("javab:" , calc(inp))
    print("done")