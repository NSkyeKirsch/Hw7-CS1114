"""
Author: Noa Kirschbaum
Assignment / Part: HW7 - Q5
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import copy

# list of numbers into an ascending list.
# don't use sorted()
# can assume no negative numbers
def get_matryoshka_list(in_list):
    temp_list = []
    final_list = []
    for i in range(len(in_list)):
        if i == 0:
            temp_list.append(in_list[i])
        else:
            if in_list[i] > in_list[(i-1)]:
                temp_list.append(in_list[i])
            else:
                final_list.append(temp_list)
                final_list = copy.deepcopy(final_list)
                temp_list.clear()
                temp_list.append(in_list[i])

    if len(temp_list) > 0:
        final_list.append(temp_list)
        final_list = copy.deepcopy(final_list)
        temp_list.clear()


    return final_list



def main():
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)
    print(matryoshka_list)

main()