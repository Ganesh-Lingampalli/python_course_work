'''
try:
    a = int(input())
    k={1:12,2:13}
    print(k[14])
    l=[234,56]
    print(l[10])
    print('l'+1)

except ValueError:
    print("Enter the correct datavalue")
except KeyError:
    print("Key is not there")
except ZeroDivisionError:
    print("Can't divide with Zero")
except IndexError:
    print("Index out of range")  
except TypeError:
    print("Enter the correct datatype")
except NameError:
    print("define the variable")
else:
    print("Error free program")
finally:
    print("End of the program")
'''
'''
try:
    k = {1:12,12:13}
    l = [232,54]
except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
'''
'''
try:
    a = int(input())
    k={1:12,2:13}
    print(k[14])
    l=[234,56]
    print(l[10])
    print('l'+1)

except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
'''
try:
    amount = int(input("Enter the amount: "))
    balance = 5000
    if amount < 0:
        raise Exception("Amount needs to be positive")
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")

