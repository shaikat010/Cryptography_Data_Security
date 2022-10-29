
s = 10
r = 4
N = 33
e = 1

x = (r**2) % N
y = (r*(s**e)) % 33


def send_e():
    e = 1
    return e

def verification(s,N,y):
    v = (s**2) % 33

    check_1 = (y**2) % 33
    check_2 = (x*(v**1)) % 33

    if(check_1 == check_2):
        print(f"Check_1 value was : {check_1}")
        print(f"Check_1 value was : {check_2}")
        print("Test Successful!")
        print("We have been able to proof without actually sending the data!")

verification(s,N,y)


