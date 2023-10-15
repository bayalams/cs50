import re

def main():
    iframe_string = input("HTML: ")

    #takes the input and passes it through the function that takes only the url part; this
    short_url = parse(iframe_string)
    #if the short url exists, then it prints it
    if short_url:
        print(short_url)
    else:
        return None

def parse(iframe_string):

    # Check if there's a YouTube link outside of an iframe
    if re.search(r"https?://(?:www\.)?youtube\.com/(?:embed/ | watch\?v=)[a-zA-Z0-9_-]+", iframe_string):
        return None

    #creates the pattern with which to compare the input, if the part exists within the input, it will match
    pattern = r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"
    match = re.search(pattern, iframe_string)

    #if it matches, returns the match formatted as follows, which will be used in the main function
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()


