import os


def command():
    print("Select an option: ")
    print("[1]: Run ex1")
    print("[2]: Run ex2")
    print("[3]: Activate stream mode")
    print("[9]: Exit")
    print("[any]: Return")
    x = input()
    return x

    x = input()

    while (True):
        x = command()
    print(x)

    if x == "1":
        os.system("python S3_ex1.py")
    elif x == "2":
        os.system("python S3_ex2.py")
    elif x == "3":
        os.system("python S3_ex3.py")
    elif x == "9":
        sys.exit()
    else:
        print('Not a valid input')
