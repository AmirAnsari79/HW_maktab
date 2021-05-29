from random import randint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", required=False, default=0)
parser.add_argument("-t", required=False, default=100)
parser.add_argument("-g", required=False, default=5)
value = parser.parse_args()
random = randint(int(value.f), int(value.t))
for i in range(int(value.g)):
    inp = int(input("guess the  number:"))
    if inp > random:
        print("guess lower:")
    elif random > inp:
        print("geuss higher:")
    else:
        print("congrats")
        break
else:
    print("you loose")
