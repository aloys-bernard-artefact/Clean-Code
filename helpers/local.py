import random

print("This code in run every time we import the file :")
print(" Importing this file.")
print(f" {__name__=}")


def dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    print("This code is run only when we run this file directly :")
    print("Rolling the dice : ", dice())
    print(f" {__name__=}")