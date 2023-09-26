def main():

    s = input("Insert string: ")
    print(shorten(s))
    return shorten(s)


def shorten(s):

    vowels = ""
    consonants = []

    for i in s:
        if i.is_alpha() == False:
            exit(1)
        elif i not in vowels:
            consonants.append(i)

    str_consonants = ''.join(consonants)
    return str_consonants

if __name__ == "__main__":
    main()

#https://submit.cs50.io/check50/a40cd9908e66e228cfe8ecd09bb93f28121fadd0