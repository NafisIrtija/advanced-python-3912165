# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """This function takes two args, doesn't do anything

    Parameters:
    arg1: the first arg, do what you want
    arg2: the second one, do what you want
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
