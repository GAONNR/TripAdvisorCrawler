# TripAdvisor Review Crawler
This is a simple python code to get the reviews from the tripadvisor web page. Requires requests, BeautifulSoup, Python 3.

## Usage
```bash
$ python crawler.py
```

To show more details while running the crawler, try

```bash
$ python crawler.py debug
```

For example, if you want to crawl Seoul Metro's Reviews, look at the url:

> https://www.tripadvisor.com/Attraction_Review-g294197-d2194168-Reviews-Seoul_Metro-Seoul.html

You can see the g code `294197`, d code `2194168`, attraction name `Seoul_Metro`, location `Seoul`.

Then open `spots.json` file and edit it like this:

```json
{
    "Seoul_Metro": {
        "location": "Seoul",
        "g": 294197,
        "d": 2194168
    }
}
```

If you want to add more attractions, you can add them in spots.json file.

After executing the code, you can see the results in results folder.
