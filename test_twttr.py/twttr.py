def main():

    s = input("Insert string: ")
    print(shorten(s))
    return shorten(s)


def shorten(s):

    vowels = "AEIOU"
    consonants = []

    for i in s:
        if i not in vowels:
            consonants.append(i)

    str_consonants = ''.join(consonants)
    return str_consonants

if __name__ == "__main__":
    main()
