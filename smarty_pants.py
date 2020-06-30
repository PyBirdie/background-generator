import re

###Smarty Pants


for number in range(1,201):
    if (number % 3) == 0:
        if (number % 5) == 0:
            print("SmartyPants")
        else:
            print("Smarty")
    elif (number % 5) == 0:
        print("Pants")
    else:
        print(number)