def is_harshad(number):
    return number % sum(int(digit) for digit in str(number)) == 0


print(is_harshad(12))
print(is_harshad(13))
