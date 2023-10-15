import re

def main():
    iframe_string = input("HTML: ")
    #takes the input and passes it through the function that takes only the url part
    short_url = parse(iframe_string)
    #if the short url exists, then it prints it
    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        return None

def parse(iframe_string):
    pattern = r"https?://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)"
    match = re.search(pattern, iframe_string)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()


