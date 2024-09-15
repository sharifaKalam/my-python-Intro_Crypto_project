import random
from sympy import isprime

#Randomly select two prime numbers
def random_numbers():
    while True:
        number = random.randint(2**15,2**16-1)
        if isprime(number):
            return number

#checking two unique prime numbers
def distinct_random_prime():       
    p= random_numbers()
    q = random_numbers()
    while q==p:
          q= random_numbers()
    return p,q

p,q= distinct_random_prime()

print(f"\nOne prime number p = {p}")
print(f"Other prime number q = {q}")