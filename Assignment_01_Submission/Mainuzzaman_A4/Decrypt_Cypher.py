alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext_input = input("Enter a String to Encrypt: ")
input_length1 = len(plaintext_input)
shift_input1 = int(input("Enter the key value:"))
print(input_length1)
output1 = ""

for i in range(input_length1):
    character = plaintext_input[i]
    location_of_string = alphabets.find(character)
    #print(location_of_string)
    new_location = (location_of_string + shift_input1) % 26

    #below if the easy way of doing the above line
    # but it will not work for every case.
    # if new_location >= 26:
    #     new_location = new_location -26

    output1 = output1 + alphabets[new_location]

print("Encrypted String: " + output1)





encryptedtext_input = input("Enter The encrypted Caeser_Cypher: ")
input_length = len(encryptedtext_input)
shift_input = int(input("Enter the key value:"))
print(input_length)
output = ""

for i in range(input_length):
    character = encryptedtext_input[i]
    location_of_string = alphabets.find(character)
    new_location = (location_of_string - shift_input) % 26
    output = output + alphabets[new_location]
print("Encrypted String: " + output)






