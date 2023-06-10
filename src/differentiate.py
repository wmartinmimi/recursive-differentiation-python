import copy


def get_equ(str):
    # return split_terms(str.split(' '))
    return [split_term(term) for term in str.split(" ") if term not in ['+', '-']]


def split_term(term):
    # split into coefficient and power
    term = term.split('x')

    # fill empty power
    if len(term) == 1:
        term = [term[0], 0]
    if term[1] == '':
        term[1] = 1

    # convert to int
    term[0] = int(term[0])
    term[1] = int(term[1])

    return term


def get_differentiated(equ):
    for i in range(0, len(equ)):
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
        if term in ['+', '-']:
            continue
        power = max(term[1], power)
    return power


def differentiate(equ):
    equ = get_equ(equ)
    print(equ)
    # create a stack of differentiated equations
    equ_stack = [equ]
    while get_max_power(equ_stack[-1]) > 1:
        new_equ = copy.deepcopy(get_differentiated(equ_stack[-1]))
        equ_stack.append(new_equ)
        print(equ_stack[-1])
