from mars import Mars
from rover import Rover

directions = ["N", "E", "S", "W"]


def validate_mars(x, y):
    """
    To validate:
    :param x: Must be an integer
    :param y: Must be an integer
    :return: True/False Value to know if inputs are validated or not.
    """
    if x.isdigit() and y.isdigit():
        mars = Mars(int(x), int(y))
        Rover.Mars = mars
        return True
    else:
        print("Only numerical elements Separated by a space. Try again!\n (eg. 5 6)")
        return False


def validate_rover(x, y, direction):
    """
    :param x: Must be an integer
    :param y: Must be an integer
    :param direction: Must be an alphabet
    :return: True/False Value to know if inputs are validated or not.
    """
    if x.isdigit() and y.isdigit() and direction.isalpha():
        return True
    return False


def validate_operations(op):
    """
    :param op: OP is the input operation. Must be a predefined set of input(eg. RRFR)
    :return: True/False; for valid and non-valid inputs.
    """
    import re
    pattern = re.compile("^[FBRL]*$")

    if pattern.match(op):
        return True
    else:
        return False


def move(op, r):
    """
    :param op: Input command for the operation.
    :param r: Rover object to giver reference to the function which is called.
    :return: No value, perform operations which is given by user.
    """
    try:
        for operation in op:
            if operation == "L":
                r.turnLeft()
            if operation == "R":
                r.turnRight()
            if operation == "F":
                r.forward()
            if operation == "B":
                r.backward()

    except Exception as err:
        op = input("Your rover went outside of Mars surface.\n"
                   "Currently the rover's position is {} facing {}. Try again!"
                   "\n>>> ".format(r.getPosition(), r.getDirection())).upper()
        move(op, r)


def main():
    flag = False
    rover = ''
    choice = input(
        "Please enter the size of mars (2 numbers, separated by a space and higher than 0.)\n>>> ").split()
    if len(choice) == 2:
        flag = validate_mars(choice[0], choice[1])
    else:
        print("Incorrect input. Please ensure you enter a string with two numerical elements")
    if flag is False:
        print('Cannot validate the input, Please change the input and try again.')
    print("\n--------------------------------------\n")
    choice = input(
        "Please enter the current rover's initial position(Two Integers and one Direction SAPARATED BY SPACE)."
        "\n(eg. 3 4 S)Remember to keep inside Mars limits!\n>>> ").split()
    if len(choice) == 3:
        if validate_rover(choice[0], choice[1], choice[2]):
            rover = Rover(int(choice[0]), int(choice[1]), choice[2])
            choice = input("Please enter the operations you wish for this rover to execute.\n>>> ").upper()
            if validate_operations(choice):
                move(choice, rover)
                print("\n--------------------------------------\n")
        else:
            print(
                "You appear to have entered an incorrect sequence. Two numbers followed by a single character (N,"
                "E,S,W)\nTry again!")
        print("--------------- Output ---------------")
        print("ROVER is on position: {} facing {}".format(rover.getPosition(),
                                                          rover.getDirection()))
        print("--------------------------------------")
        exit()


if __name__ == "__main__":
    main()
