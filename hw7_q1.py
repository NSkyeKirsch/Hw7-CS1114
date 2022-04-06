"""
Author: Noa Kirschbaum
Assignment / Part: HW7 - Q1
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

#take in list of frequencies
#take in a string of new DNA sequence
#update previous list numbers to reflect their added frequencies
#print the nucleotides being added to each frequency
def update_frequencies(old_frequency_list, new_dna_seq):

    count_list = [new_dna_seq.count('A'),new_dna_seq.count('C'),new_dna_seq.count('T'),new_dna_seq.count('G')]

    for i in range(len(old_frequency_list)):
        #this is equal to the first tuple [zero,one]
        list_of_tup_at_i = list(old_frequency_list[i])
        #change the number in the tuple to reflect the new added amount
        list_of_tup_at_i[1] += count_list[i]
        #change the list into a tuple and replace the old tuple
        old_frequency_list[i] = tuple(list_of_tup_at_i)

    print("A -> {} | C -> {} | T -> {} | G -> {}".format(count_list[0], count_list[1], count_list[2], count_list[3]))

    return old_frequency_list






def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)
    print(new_frequencies)
main()

