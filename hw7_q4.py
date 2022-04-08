"""
Author: Noa Kirschbaum
Assignment / Part: HW7 - Q4
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import super_secret_module

def is_impostor(information, corrupter_function):
    # find out if the list is deep or shallow (True if deep)
    # information is original list

    information.insert(0, ['a', 'b', 'c'])

    corrupted_list_of_stuff = corrupter_function(information)

    information[0][1] = 2

    print(information)
    print(corrupted_list_of_stuff)

    if information[0][1] != corrupted_list_of_stuff[0][1]:
        return True
    else:
        return False


def main():
    original_list = [1, 2, 3]

    print(is_impostor(original_list, super_secret_module.corrupter))

main()