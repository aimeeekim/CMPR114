def main():
    try:
        string = input('Enter string: ')
        shift_amount = int(input('Enter shift amount: '))
        print('The encrypted string is: ',get_caesar_cipher(string, shift_amount))

    except Exception as err: 
        print(err)

def get_caesar_cipher(string, shift_amount):
    encrypted_string = ''
    new_word = ''
    string1 = string.upper()
    word_list = string1.split() 

    try:
        for word in word_list:
            for char in word:
               
                char_position = ord(char) - ord('A')

                new_char_position = (char_position + shift_amount) % 26

                new_char_decimal = new_char_position + ord('A')        
               
                new_char = chr(new_char_decimal)

                new_word += new_char

            encrypted_string += new_word + ' '

            new_word = ''

        if string.islower():
            encrypted_string = encrypted_string.lower()
        else:
            encrypted_string

        return encrypted_string

    except Exception as err:  
        print(err)

main()