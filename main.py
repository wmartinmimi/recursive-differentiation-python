from src.differentiate import differentiate

# equation format
# [[coefficient, power], operator, ...]


def main():
    print('Enter equation')
    # eg. 4x3 + 3x - 2
    
    equation = input('> ')
    differentiate(equation)


if __name__ == '__main__':
    main()