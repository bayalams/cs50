def main():

    s = input("Insert string: ")


def shorten(s):

    print(s)
    vowels = "aeiouAEIOU"
    consonants = []

    for i in s:
        if i not in vowels:
            consonants.append(i)

    str_consonants = ''.join(consonants)
    print(str_consonants)
    return str_consonants

