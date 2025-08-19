def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num1 = int(input("enter a first numbeer : "))
num2 = int(input("enter a 2nd  number : "))
if is_prime(num1):
    print("num1 is a prime number ")
else:
    print("num1 is not prime ")
    if is_prime(num2):
        print("num2 is a prime number ")
    else:
        print("numb2 is not a prime number ")
