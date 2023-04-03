def main():
    
    string = input('enter a sentence: ')
    print('Pig Latin: ',get_pig_latin(string))

def get_pig_latin(string):
    string = string.upper()
    word_list = string.split()      
    pig_latin = ''

    try:
        for word in word_list:         
            pig_latin += word[1:] + word[0] + 'AY '   
                                                      
        return pig_latin

    except Exception as err:  
        print(err)

main()