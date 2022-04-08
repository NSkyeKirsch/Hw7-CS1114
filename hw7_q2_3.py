"""
Author: Noa Kirschbaum
Assignment / Part: HW7 - Q2 + Q3
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def is_haiku(original_string):
    real_haiku = False
    message = ""
    each_line_list = original_string.split("/")
    if len(each_line_list) == 3:
        line_one = each_line_list[0].split(",")
        line_two = each_line_list[1].split(",")
        line_three = each_line_list[2].split(",")

        if len(line_one) == 5:
            if len(line_two) == 7:
                if len(line_three) == 5:
                    real_haiku = True
                else:
                    message = "WARNING: The third line is not 5 syllables long."
            else:
                message = "WARNING: The second line is not 7 syllables long."
        else:
            message = "WARNING: The first line is not 5 syllables long."
    else:
        message = "WARNING: This does not have 3 lines."

    return message + "\n" + str(real_haiku) if real_haiku == False else str(real_haiku)


def main():

    sample_input_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
    print(is_haiku(sample_input_string))

main()