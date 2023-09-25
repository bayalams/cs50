from twttr import shorten

def test_shorten():

    if shorten("macaco") != "mcc":
        print("not mcc")
    else:
        print("test passed")