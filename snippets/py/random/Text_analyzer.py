# Translated version

import random
contra = input()
abcd = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# FirstItem ->
FirstItem = f"1. Input: '{contra}'"


# SecondItem ->
pass_length = len(contra)

SecondItem = f"2. Input contains: {pass_length} characters"


# ThirdItem -> 
def hasher(contra):

    out = ""
    for i in contra:

        out += str(str(ord(i) * 3 // 5 - 1) + random.choice(str(abcd))) 

    return out[0:11]

hashed_input = hasher(contra)

ThirdItem = f"3. Hashed input: '{hashed_input}'"


# FourthItem ->
list_element = []

def list_inator(contra):
    if ' ' in contra:

        list_element = contra.split()
        return f"4. The input text can be divided into {len(list_element)} elements: \n\t\t{list_element}"
    else:

        return '4. Input contains no spaces.'

FourthItem = list_inator(contra)


# FifthElement ->
def thing_with_tf(contra):
    if ' ' in contra:
        return False
    else:
        if contra.isalpha() == False:
            if len(contra) >= 8 and abcd in contra :
                return True
            else:
                return False
        else:
            return False

FifthElement = f'5. Is it a safe (8 Char & ≥ 1 letters w/o spaces) password? : \n\t\t{thing_with_tf(contra)}'


# LastOutput ->
LastOutput = f"\t{FirstItem}\n\n\t{SecondItem}\n\n\t{ThirdItem}\n\n\t{FourthItem}\n\n\t{FifthElement}"

print("Input analyzed, these are the results:\n\n" + LastOutput)
