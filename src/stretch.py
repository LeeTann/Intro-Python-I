# Prime numer is a natural number greater than 1 that cannot be formed by muliplying two smaller natural numbers.
# ex. 5 is a prime because it can only be formed with 1 x 5 or 5 x 1.
# ex. 6 is not a prime because it is a product of 2 x 3 which are both smaller than 6.

user_num = int(input("Please enter a number to see if it's prime: "))

# Check if given number is greater than 1
if user_num > 1:

  # Iterate from 2 to n/2
  for i in range(2, user_num // 2):

    # If num is divisible by any number between 2 and n/2, it is not a prime number
    if (user_num % i) == 0:
      print(user_num, "is NOT a prime number")
      break
  else:
    print(user_num, "is a prime number")
else:
  print(user_num, "is not a prime")