import random
from sympy import isprime

phi_of_N=2875045536
# Randomly select a public-key- e
def define_public_key_e ():
        public_key_number = random.randint(1, phi_of_N-1)
        return public_key_number

#checking public key e and Phi(N) are coprime or not(gcd(e, Phi(N)) =1).
def gcd_of_two_number():
    public_key_e= define_public_key_e()

    t=public_key_e
    d=phi_of_N
    while t!=0:
          w=d%t
          d=t
          t=w
    if d!= 1:
        
        return gcd_of_two_number()       
    else:
        return public_key_e,d

public_key_e, gcd= gcd_of_two_number()
print(f"public key, e = {public_key_e}")
print(f"gcd(e , phi(N))= 1\ngcd( {public_key_e},{phi_of_N} )= {gcd}")