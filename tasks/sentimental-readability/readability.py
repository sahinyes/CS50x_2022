from cs50 import get_string

i = 0
letter = 0
word = 1
satz = 0
excl = [".","!","?"]

text = get_string("Type text: ")

while i < len(text):

    if (text[i].isalpha()):

        letter += 1
        i += 1

    elif (text[i] == " "):

        word += 1
        i +=1

    elif (text[i] == excl[0] or text[i] == excl[1] or text[i] == excl[2]):

        satz += 1
        i += 1
    else:
        i += 1

L = letter / word * 100
S = satz / word * 100

index = round(0.0588 * L - 0.296 * S - 15.8)


if (index < 1):
    print("Before Grade 1")

elif (index >16):
    print("Grade 16+")

else:
    print(f"Grade {index}")