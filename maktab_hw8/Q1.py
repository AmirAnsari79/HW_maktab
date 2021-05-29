import sys

(sys.argv).pop(0)
x = 0
res = 0
for i in range(len(sys.argv)):
    x = x + int(sys.argv[i])
    res = x / len(sys.argv)
print(res)

# seq2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", nargs="+", required=True)
parser.add_argument("-f", required=False, default="2")
value = parser.parse_args()
x = 0
for i in range(len(value.g)):
    x = x + int(value.g[i])
    res = round(x / len(value.g), int(value.f[0]))
print(res)
