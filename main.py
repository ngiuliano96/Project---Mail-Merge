PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name.lower()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

