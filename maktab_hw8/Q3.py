from datetime import datetime, timedelta

inp1 = input("enter first date:")
inp2 = input("enter second date:")
inp3 = input("enter a day:")

x = inp1.split("/")
z = inp2.split("/")

b1 = datetime(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]))
b2 = datetime(int(z[0]), int(z[1]), int(z[2]), int(z[3]), int(z[4]), int(z[5]))
new_date = b1
x = b1.weekday()
print(x)
if x > int(inp3):
    new_date += timedelta(x - int(inp3))
else:
    new_date += timedelta(7 - (int(inp3) - x))
while new_date < b2:
    new_date += timedelta(7)
    print(new_date)
