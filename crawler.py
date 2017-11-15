from bs4 import BeautifulSoup
import requests
import json
import sys

def get_spots_info(filename, debug=False):
    data = dict()
    with open(filename) as f:
        data = json.load(f)

    if debug:
        print('====== Spots Info ======')
        print(data)

    return data

def generate_url(spots_info, spot, num):
    review_url_front = 'https://www.tripadvisor.com/Attraction_Review-g%s-d%s-Reviews-' % \
            (spots_info[spot]['g'], spots_info[spot]['d'])
    review_url_back = '%s-%s.html' % (spot, spots_info[spot]['location'])

    return '%s%s%s' % (review_url_front, num, review_url_back)

def get_reviews(spots_info, debug=False):
    spots = spots_info.keys()
    review_nums = ['or%d-' % (_ * 10) for _ in range(5)]
    review_nums[0] = ''

    for spot in spots:
        review_urls = list()

        f = open('result/%s-%s.txt' % (spot, spots_info[spot]['location']), 'w')

        if debug:
            print('====== URL ======')

        for num in review_nums:
            url = generate_url(spots_info, spot, num)

            if debug:
                print(url)

            rspns = requests.get(url)

            soup = BeautifulSoup(rspns.text, 'html.parser')
            reviews = soup.select('.review-container .review')
            quotes = soup.select('.review-container .review .quote a')
            review_urls += list(map(lambda x: x['href'], quotes))

        if debug:
            print('====== Reviews ======')

        for review_url in review_urls:
            rspns = requests.get('https://www.tripadvisor.com%s' % review_url)

            soup = BeautifulSoup(rspns.text, 'html.parser')
            review = soup.select('.review')[0]
            quote = review.select('.noQuotes')[0].get_text().encode('utf-8')
            review_text = review.select('.partial_entry')[0].get_text().encode('utf-8')

            if debug:
                print(quote)
                print(review_text)

            f.write(quote)
            f.write('\n')
            f.write(review_text)
            f.write('\n')

        f.close()

if __name__ == '__main__':
    debug = False
    if 'debug' in sys.argv[1:]:
        debug = True

    spots_info = get_spots_info('spots.json', debug)
    get_reviews(spots_info, debug)
