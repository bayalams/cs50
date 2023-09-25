from twttr import shorten

def test_shorten():

    if shorten("macaco") != "mcc":
        print("not mcc")

if __name__ == "_main__" :
    test_shorten()