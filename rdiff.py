import copy

# equation format
# [[coefficient, power], operator, ...]

def get_equ(str):
    equ = str.split(" ")
    return split_terms(equ)

def split_terms(equ):
    for i in range(0, len(equ)):
        term = equ[i]
        # skip operators
        if term == '+':
            continue
        if term == '-':
            continue
        # split into coefficient and power
        equ[i] = term.split('x')
        # fill empty power
        if len(equ[i]) == 1:
            equ[i] = [equ[i][0], 0]
        if equ[i][1] == '':
            equ[i][1] = 1
        # convert to int
        equ[i][0] = int(equ[i][0])
        equ[i][1] = int(equ[i][1])
    return equ

def get_differentiated(equ):
    # make sure i don't modify the original equation
    equ = copy.deepcopy(equ)

    for i in range(0, len(equ)):
        # skip operators
        if equ[i] == '+':
            continue
        if equ[i] == '-':
            continue

        # get coefficient and power
        if i - 1 < 0:
            co = equ[i][0]
        else:
            if equ[i-1] == '+':
                co = equ[i][0]
            else:
                co = -equ[i][0]
        power = equ[i][1]

        # calculate differentiated
        new_co = co * power
        new_power = power - 1

        # insert results
        equ[i][0] = new_co
        equ[i][1] = new_power
    return equ

def get_max_power(equ):
    power = 0
    for term in equ:
        if term == '+':
            continue
        if term == '-':
            continue
        power = max(term[1], power)
    return power

# main program
print('enter equation')
# eg. 4x3 + 3x - 2
str = input('> ')
equ = get_equ(str)
print(equ)
# create a stack of differentiated equations
equ_stack = [equ]
while get_max_power(equ_stack[-1]) > 1:
    equ_stack.append(get_differentiated(equ_stack[-1]))
    print(equ_stack[-1])
# end of program
