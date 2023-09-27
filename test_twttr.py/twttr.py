
def main():

    s = input("Insert string: ")
    print(shorten(s))
    return shorten(s)


def shorten(s):

    vowels = "eiouAEIOU"
    consonants = []

    for i in s:
        if i.isalpha() == False:
            print("not a word")
            exit(1)
        if i not in vowels:
            consonants.append(i)

    str_consonants = ''.join(consonants)
    return str_consonants

if __name__ == "__main__":
    main()

