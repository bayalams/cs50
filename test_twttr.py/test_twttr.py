from twttr import shorten

def test_shorten():

    assert shorten("macaco") == "mcc"

if __name__ == "__main__":
    test_shorten()