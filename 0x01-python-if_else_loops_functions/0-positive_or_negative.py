#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive = "is positive"
zero = "is zero"
negative = "is negative"
if number < 0:
print("{}{}".format(number, negative))
elif number == 0:
print("{}{}".format(number, zero));
else:
print("{}{}".format(number, positive))
