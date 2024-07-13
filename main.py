
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    input_str = input("Enter multiple values separated by spaces: ")
    return [int(value) for value in input_str.split()]


def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    reversed_list = []
    while numbers:
        reversed_list.append(numbers.pop())
    return reversed_list


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
