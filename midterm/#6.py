number_list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def get_lucky_number(array):
    lucky_number = 27
    lucky_number_found = False
    for number in array:
        if number == lucky_number:
            lucky_number_found = True

    return lucky_number_found

def print_message(is_found):
    if is_found:
        print("Number 27 is found.")
    else:
        print("The lucky number is not found in this list.")


print_message(get_lucky_number(number_list))