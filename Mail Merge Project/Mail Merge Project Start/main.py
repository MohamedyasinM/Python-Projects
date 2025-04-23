from dataclasses import replace

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as nf:
    contentss = nf.readlines()


with open("./Input/Letters/starting_letter.txt", mode="r") as sf:
    content = sf.read()
    for name in contentss:
        sp = name.strip()
        new_l = content.replace(PLACEHOLDER, sp)
        with open(f"./Output/ReadyToSend/letter_for_{sp}.txt",mode="w") as lf:
            lf.write(new_l)


