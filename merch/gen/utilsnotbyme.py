# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
def check(num):
  num2 = int(num)
  if (num2 % 2) == 0:
    print("{0} is Even".format(num2))
    data = "even"
    return data
  else:
    print("{0} is Odd".format(num2))
    data = "odd"
    return data
