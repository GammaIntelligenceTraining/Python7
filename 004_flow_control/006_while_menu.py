# https://et.wikipedia.org/wiki/Isikukood
while True:
    try:
        user_input = input('Please enter you ID (type exit to quit): ')
        if user_input.lower() == 'exit':
            break
        int(user_input)
        if len(user_input) != 11:
            if len(user_input) > 11:
                print('ID is too long!')
            else:
                print('ID is too short!')
            raise UserWarning
    except ValueError:
        print('ID you entered is not numeric!')
    except UserWarning:
        print('ID you entered is not 11 digits long')
    else:
        print(user_input)
        break