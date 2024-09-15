import math

N = 2875154287
public_key_e=2475435379
phi_of_N =2875045536

def private_key_helper(a,b,q):
    x= a - (b * q)
    return x
#computing private key
def compute_private_key_d():
    t=public_key_e
    d=phi_of_N
    a=0
    b=1
    while t!=1:
        w=d%t
        q = math.floor(d/t)
        r = private_key_helper(a, b, q)
        a = b
        b = r
        d=t
        t=w
        # print(w,d,t,r)

    if r > 1 and r < phi_of_N :
        private_key_d=r
        print(f"\nprivate key, d={private_key_d}")
    else:
        private_key_d=phi_of_N   - (-r)
        print(f"\nprivate key, d={private_key_d}")
    return private_key_d

private_key_d =compute_private_key_d()

# convert string to hexa
def string_to_hex(str):
    hexa_str = ""
    for char in str:
        hex_value = format(ord(char), '02x')
        hexa_str += hex_value
    return hexa_str
# converting the strings to hexadecimals
message='BEST OF LUCK IBE'
strings_to_convert = ['BES', 'T O', 'F L', 'UCK', 'IBE']
string_to_hexa = [string_to_hex(str) for str in strings_to_convert]
#print(f'\nstring conversion from string to hexadecimals =\n{string_to_hexa}')

# convert the hexadecimals to integers
hexa_to_int = [int(string_to_hexa, 16) for string_to_hexa in string_to_hexa]
#print(f'string conversion from hexadecimals to integers=\n {hexa_to_int}\n')

# Message Encryption
int_values_of_m=  hexa_to_int 
partner_e = 1526166685
partner_N = 3247314737

def message_encryption(int_values_of_m, partner_e, partner_N):
    result = 1
    int_values_of_m = int_values_of_m % partner_N
    while partner_e > 0:
        if partner_e % 2 == 1:
            result = (result * int_values_of_m) % partner_N
        partner_e = partner_e >> 1 
        int_values_of_m = (int_values_of_m * int_values_of_m) % partner_N
    return result

result = [message_encryption(int_values_of_m,partner_e, partner_N) for int_values_of_m in int_values_of_m]
print(f'My CIPHERTEXT = {result}')

# Message Decryption
partner_ciphertext=[2367520010, 361900205, 2771163958, 2162736234, 2798309448]
print(f'\nPARTNER_CIPHERTEXT={partner_ciphertext}')
def message_decryption(partner_ciphertext, private_key_d, N):
    result = 1
    partner_ciphertext = partner_ciphertext % N
    while private_key_d > 0:
        if private_key_d % 2 == 1:
            result = (result * partner_ciphertext) % N
        private_key_d = private_key_d >> 1 
        partner_ciphertext = (partner_ciphertext* partner_ciphertext) % N
    return result

decrypted_int_m = [message_decryption(partner_ciphertext,private_key_d,N) for partner_ciphertext in partner_ciphertext]
#print(f'decrypted integer message = {decrypted_int_m}')

 # convert the integer to hexadecimals
int_to_hexa = [hex(decrypted_int_m)[2:] for decrypted_int_m in decrypted_int_m]
#print(f'integer to hexa = {int_to_hexa}') 

decrypted_strings_chunk = [bytes.fromhex(int_to_hexa).decode() for int_to_hexa in int_to_hexa]
print(f'\nPARTNER_MESSAGE_chunks_AFTER_DECRYPT= {decrypted_strings_chunk}')
decrypted_message = ''.join(decrypted_strings_chunk)
print(f'\nPARTNER_MESSAGE_AFTER_DECRYPT= "{decrypted_message}"')

#Signature
my_sign='SHARIFA AKTER'
my_signed_chunks = ['SHA', 'RIF', 'A A', 'KTE', 'R']
#convertion from string to hexadecimals
string_to_hexa_s = [string_to_hex(my_signed_chunks) for my_signed_chunks in my_signed_chunks]
#print(f'string to hexa ={string_to_hexa_s}')

# convert the hexadecimals to integers
hexa_string_s = string_to_hexa_s
hexa_to_ints = [int(hexa_string_s, 16) for hexa_string_s in hexa_string_s]
#print(f'hexa to integer ={hexa_to_ints}')
my_sign_text = hexa_to_ints
#print(my_sign_text)
results = [message_encryption(my_sign_text,private_key_d,N) for my_sign_text in my_sign_text]
print(f'\nMy Signed Text = {results}\n')

#Verification
partner_signed_text=[3174650564, 2970577645, 2391020763, 217065856]
print(f'Partner signed text ={partner_signed_text}')
signed_int_m = [message_decryption(partner_signed_text, partner_e, partner_N) for partner_signed_text in partner_signed_text]
print(f'Decrypted signed(integer) message = {decrypted_int_m}')
# convert the integer to hexadecimals
int_to_hexa1 = [hex(signed_int_m)[2:] for signed_int_m in signed_int_m]
#print(f'integer to hexa = {int_to_hexa1}') 

decrypted_strings_chunk1 = [bytes.fromhex(int_to_hexa1).decode() for int_to_hexa1 in int_to_hexa1]
print(f'Partner Signed Message chunk After Decryption= {decrypted_strings_chunk1}')
decrypted_message1 = ''.join(decrypted_strings_chunk1)
print(f'Partner Signed Message After Decryption= "{decrypted_message1}"')

partner_original_text = 'OBINNA IBE'
if(partner_original_text == decrypted_message1):
    IS_VALID_SIGNATURE = 'True'
    print (f'IS_VALID_SIGNATURE = {IS_VALID_SIGNATURE}')
else:
    IS_VALID_SIGNATURE ='False'
    print (f'IS_VALID_SIGNATURE = {IS_VALID_SIGNATURE}')