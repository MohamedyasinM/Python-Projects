

import pandas

data  = pandas.read_csv("nato_phonetic_alphabet.csv")

letters_dict = {row.letter : row.code for (index,row) in data.iterrows()}




def op():
    user_input = input("What is your name ").upper()
    try:
        output_list = [letters_dict[i] for i in user_input]
    except KeyError:
        print("Please enter alphabets only")
        op()
    else:
        print(output_list)

op()