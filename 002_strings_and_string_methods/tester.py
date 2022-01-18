isikukood = input("Please enter ID: ")
if len(isikukood) == 11:
    print('ID is OK')
elif len(isikukood) > 11:
    print('ID is too long')
else:
    print('ID is too short')

if len(isikukood) != 11:
    if len(isikukood) > 11:
        print('ID is too long')
    else:
        print('ID is too short')
else:
    print('ID is OK')
