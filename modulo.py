def find_mod_inv(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('The modular inverse does not exist.')

a = 17
m = 203
try:
    res=find_mod_inv(a,m)
    print("The required modular inverse is: "+ str(res))
except:
    print('The modular inverse does not exist.')

