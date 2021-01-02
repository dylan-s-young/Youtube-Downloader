### TRY/EXCEPT CASES

def is_digit(num):
    '''
    Tests if input is num. 
    '''
    while True:
        try:
            num = int(num)
            break
        except ValueError:
            num = input("That was not an integer or your input exceeds the index.\n")
        
    return num


            