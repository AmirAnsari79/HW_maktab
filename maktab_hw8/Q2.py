import argparse
from datetime import datetime, time
import jdatetime

parser = argparse.ArgumentParser()
parser.add_argument("-input", nargs="+", required=True)
parser.add_argument("-week", required=True)
value = parser.parse_args()

x = value.input[0].split("/")
z = value.input[1].split("/")
b1 = datetime(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]))
b2 = datetime(int(z[0]), int(z[1]), int(z[2]), int(z[3]), int(z[4]), int(z[5]))
c = b2 - b1
cdays = int(abs(c.days))
b11 = jdatetime.datetime.fromgregorian(day=int(x[2]), month=int(x[1]), year=int(x[0]), hour=int(x[3]), minute=int(x[4]),
                                       second=int(x[5]))
b22 = jdatetime.datetime.fromgregorian(day=int(z[2]), month=int(z[1]), year=int(z[0]), hour=int(z[3]), minute=int(z[4]),
                                       second=int(z[5]))

print(cdays * 24 * 60 * 60 + c.seconds)
print("khabise:", round(cdays / (4 * 365)), "daylight:", round(cdays / (6 * 30)))
print("shamsi:", b11, b22)
