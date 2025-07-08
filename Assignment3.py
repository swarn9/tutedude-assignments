# _________________________ Task_1________________________________________#

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

sample_number = int(input("Enter a number: "))
print("Factorial of", sample_number, "is", factorial(sample_number))

# __________ By using the loop___________________________#
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *=i
    return result
sample_number = int(input("Enter a number: "))
print("Factorial of", sample_number, "is", factorial(sample_number))


#______________________________Task_2_________________________#

import math
number = float(input("Enter a positive number : "))
if number <= 0:
    print("Enter a number greater than 0")
else:
    Sqrt_number = math.sqrt(number)
    log_number = math.log(number)
    sine_number = math.sin(number)
    print(f'square root: {Sqrt_number}')
    print(f'logarithm : {log_number}')
    print(f'Sine : {sine_number}')