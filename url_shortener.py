import random
import string

class URLShortener:
    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}
        self.domain = "short.url/"

    def shorten_url(self, long_url):
        if long_url in self.long_to_short:
            return self.domain + self.long_to_short[long_url]

        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(6))
        short_url = self.domain + short_code

        self.short_to_long[short_code] = long_url
        self.long_to_short[long_url] = short_code

        return short_url

    def get_original_url(self, short_url):
        short_code = short_url.split('/')[-1]
        if short_code in self.short_to_long:
            return self.short_to_long[short_code]
        else:
            return None

# Example usage:
if __name__ == "__main__":
    shortener = URLShortener()

    long_url_1 = "https://www.example.com/article/how-to-shorten-urls"
    long_url_2 = "https://www.example.com/blog/python-tips-and-tricks"

    short_url_1 = shortener.shorten_url(long_url_1)
    short_url_2 = shortener.shorten_url(long_url_2)

    print("Shortened URL 1:", short_url_1)
    print("Shortened URL 2:", short_url_2)

    original_url_1 = shortener.get_original_url(short_url_1)
    original_url_2 = shortener.get_original_url(short_url_2)

    print("Original URL 1:", original_url_1)
    print("Original URL 2:", original_url_2)