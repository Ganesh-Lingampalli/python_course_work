'''
fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friends: "))
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account first")
    '''

'''
reg = eval(input("Registeration: "))
if reg:
    fp = eval(input("Fee paid: "))
    if fp:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")
    '''

la = eval(input("Link Active: "))
if la:
    pg = eval(input("Permission Granted: "))
    if pg:
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")
