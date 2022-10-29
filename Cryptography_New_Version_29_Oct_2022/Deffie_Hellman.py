# This is the deffie hellman secure key exchange protocol
Alice = 5
Bob = 12
g = 2
P = 29

A = (g**Alice)%P
print(A)

B = (g**Bob)%P
print(B)


def send_to_Alice(B):
    Alice_Generate = ((g**Bob)**Alice) % P
    return Alice_Generate

def send_to_Bob(A):
    Bob_Generate = ((g**Alice)**Bob) % P
    return Bob_Generate

if(send_to_Alice(B) == send_to_Bob(A)):
    print("Sharing key is successful!")
    print(f"The shared key is {send_to_Bob(A)}!")

else:
    print("SHaring key is unsuccessful!")



