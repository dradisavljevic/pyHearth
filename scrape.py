import pandas as pd
import bs4
import config as cfg
import utility
import urllib.request


def main():
    '''
    Module used for gathering URLs of the decks listed on Hearthstone Top Decks Website.
    '''
    deck_list = {}

    for season_number in range(1, utility.calculate_season() + 1):
        weburl = cfg.SCRAPE_URL + str(season_number)
        req = urllib.request.Request(weburl, headers={'User-Agent': 'Mozilla/5.0'})

        page = urllib.request.urlopen(req).read()
        soup = bs4.BeautifulSoup(page, 'html.parser')

        print('Extracting Season ' + str(season_number) + ' Decks:')

        links = soup.find_all('h4')
        for link in links:
            deck_title = link.text.strip()
            link = link.find('a')
            deck_list[link['href']] = deck_title

        pages = soup.find('span', {'class': ['page-link', 'pages']})
        page_text = pages.text.strip().split(' ')
        last_page = page_text[-1]

        utility.printProgressBar(1, int(last_page), prefix = 'Progress:', suffix = 'Complete', length = 50)

        for i in range(2, int(last_page) + 1):
            weburl = cfg.SCRAPE_URL + str(season_number) + '/page/' + str(i)
            weburl = cfg.SCRAPE_URL + str(season_number)
            req = urllib.request.Request(weburl, headers={'User-Agent': 'Mozilla/5.0'})

            page = urllib.request.urlopen(req).read()
            soup = bs4.BeautifulSoup(page, 'html.parser')
            links = soup.find_all('h4')
            for link in links:
                deck_title = link.text.strip()
                link = link.find('a')
                deck_list[link['href']] = deck_title
            utility.printProgressBar(i, int(last_page), prefix = 'Progress:', suffix = 'Complete', length = 50)

    print('Finished acquiring deck urls.')
    decks_to_csv(deck_list)


def decks_to_csv(deck_list):
    '''
    Scrapes information from the collected decks URLs and writes it to a CSV file.
    Args:
        deck_list   - Required  : list of deck urls collected inside the main module.
    '''
    data = pd.DataFrame(columns=cfg.DECKS_TITLE)
    print('Now extracting information on the acquired decks:')
    i = 1
    for url, name in deck_list.items():
        utility.printProgressBar(i, len(deck_list), prefix = 'Progress:', suffix = 'Complete', decimals = 2, length = 50)
        i = i + 1
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        page = urllib.request.urlopen(req).read()
        soup = bs4.BeautifulSoup(page, 'html.parser')
        deck_code = soup.find('button', {'id': 'deck-code'})['data-deck-code']
        rating = soup.find('div', {'class': 'rating-scores'}).text.strip().replace('+', '')
        date = soup.find(True, {'class': ['entry-date', 'published']}).text.strip()
        uploader = soup.find(True, {'class': ['author', 'vcard']}).text.strip()

        deck_meta_stats = soup.find('div', {'class': 'deck-meta'})
        meta_links = deck_meta_stats.find_all('a')
        deck_class = None
        deck_format = None
        deck_type = None
        deck_season = None
        deck_style = None

        for link in meta_links:
            if link.text.strip() in cfg.CLASS_LIST:
                deck_class = link.text.strip()
                continue
            elif link.text.strip().capitalize() in cfg.DECK_FORMATS:
                deck_format = link.text.strip().capitalize()
                continue
            elif link.text.strip().capitalize() in cfg.DECK_TYPES:
                deck_type = link.text.strip().capitalize()
                continue
            elif link.text.strip().split('-')[0] == 'season':
                deck_season = link.text.strip().split('-')[1]
                continue
            elif link.text.strip().capitalize() in cfg.DECK_STYLES:
                deck_style = link.text.strip().capitalize()
                continue
        dust = soup.find('div', {'class': 'deck-info'}).text.strip().split(' ')[-1].split('\n')[0].replace(',','')

        row = [deck_season, name, deck_class, deck_code, url, dust, rating, uploader, date, deck_format, deck_type, deck_style]
        data.loc[data.shape[0]] = row

    data = data.sort_values(cfg.DECKS_SORT_COLUMN)
    data.to_csv(cfg.DECKLIST_CSV, index=False)
    print('All finished. Decks saved to a CSV file.')

if __name__ == '__main__':
    main()
