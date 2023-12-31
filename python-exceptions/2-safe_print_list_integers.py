#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            count += 1    
        except (ValeuError, TypeError):
            continue
    print("")
    return count
    