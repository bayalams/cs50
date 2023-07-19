def main():
    s = input("insert string")
    convert(s)


def convert(s_1):

    for i in s_1:
        if i == ":(" or i == ":)":
            i.replace(":(", "🙁") or i.replace(":)", "🙂")

    return s_1