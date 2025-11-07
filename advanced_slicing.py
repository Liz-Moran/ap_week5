def advanced_slice():
    # Advanced Slicing:
    # Given the string 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # a. Extract the letters 'hij'.
    print(alphabet[7:10])
    # b. Extract every second letter starting from 'a' to 'm'.
    every_second_letter=alphabet[0:13:2] 
 # c. Reverse the entire string using slicing.
    reversed_alphabet = alphabet [::-1]
    print(reversed_alphabet)
    
