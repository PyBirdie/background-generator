import re

def list_fun(list):
    # Check that list is only int/real numbers and return error if otherwise
    for number in list:
        if type(number) != int:
            print("NO FUN: Please provide a list with only integer numbers.")
            return
        
    print("median = " + str(list[int(len(list)/2)]))
    print("average = " + str(sum(list)/len(list)))
    print("sum = " + str(sum(list)))
    
    descending_sorted = sorted(list)
    descending_sorted.sort(reverse=True)
    print("descending_sorted = " + str(descending_sorted))
    
    both_1_and_5 = []
    either_1_or_5 = []
    for number in list:
        if (re.search("[15]",str(number))):
            either_1_or_5.append(number)
        if (re.search("1",str(number))) and (re.search("5",str(number))):
            both_1_and_5.append(number)
    print("both_1_and_5 = " + str(both_1_and_5))
    print("either_1_or_5 = " + str(either_1_or_5))
    
    return
    

###Smarty Pants


for number in range(1,102):
    if (number % 3) == 0:
        if (number % 5) == 0:
            print("SmartyPants")
        else:
            print("Smarty")
    elif (number % 5) == 0:
        print("Pants")
    else:
        print(number)