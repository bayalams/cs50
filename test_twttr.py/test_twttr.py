from twttr import shorten

def test_shorten():

    shorten("macaco") == "mcc"
    shorten("OrangoTango") == "rgTng"