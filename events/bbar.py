import ast
import bs4
from datetime import datetime
import re
import requests
import unicodedata


def fetch_page_soup(url):
    r = requests.get(url)
    content = r.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    return soup


def parse_event_cost(event_cost):
    if event_cost == "Donation":
        event_cost = event_cost.replace("Donation", "0")
        return event_cost
    else:
        currency_re = re.compile(r'(?:[\$]{1}[,\d]+.?\d*)')
        event_cost = re.findall(currency_re, event_cost)
        if len(event_cost) > 0:
            event_cost = event_cost[0].split(".")[0].replace("$", '')
            event_cost = ''.join(s for s in event_cost if s.isdigit())
            return event_cost
        else:
            return ''


def handle_ans_page(soup):


    return


def get_event_description(url):
    soup = fetch_page_soup(url)
    events_url = soup.find('meta', {'property': 'og:description'})['content']

    return events_url


def main():
    current_date = datetime.today()
    url = "https://bbardc.org/events/month/"
    soup = fetch_page_soup(url)
    events = handle_ans_page(soup)

    return events


if __name__ == '__main__':
    events = main()


