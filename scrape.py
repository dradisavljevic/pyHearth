import pandas as pd
import bs4
import config as cfg
import utility
import urllib.request
from multiprocessing import Pool, cpu_count
from tqdm import tqdm


def main():
    '''
    Main module. Calls other modules in parallel and saves extracted data into a csv file.
    '''
    
    p = Pool(cpu_count() - 1)
    seasons = list(range(1, utility.calculate_season() + 1))
    print('Extratcting decks by season. Please wait.')
    deck_dict_list = list(tqdm(p.imap(gather_deck_info, seasons), total = len(seasons)))
    p.terminate()
    p.join()

    deck_dict = {}
    deck_dict = {k:v for x in deck_dict_list for k,v in x.items()} # Merge list of dictionaries into a single dictionary

    deck_list = []
    for url, name in deck_dict.items():
        if url in cfg.INVALID_URLS:
            continue
        deck_list.append(str(url) + '$$$$$$$$' + str(name)) # Combination of characters highly unlikely to be part of deck name and URL is used to connect the two strings

    p = Pool(cpu_count() - 1)
    print('Now extracting information on the extracted decks. Please wait.')
    deck_information_dataframes = list(tqdm(p.imap(decks_to_csv, deck_list), total = len(deck_list)))
    p.terminate()
    p.join()

    deck_information_dataframe = pd.concat(deck_information_dataframes) # Merge dataframes from the list into a single one
    deck_information_dataframe.SEASON = pd.to_numeric(deck_information_dataframe.SEASON, errors='coerce') # Convert the column values to integer
    deck_information_dataframe = deck_information_dataframe.sort_values(cfg.DECKS_SORT_COLUMN) # Sort them by chosen column
    deck_information_dataframe.to_csv(cfg.DECKLIST_CSV, index=False)

    print('All finished. Decks saved to a CSV file.')



def gather_deck_info(season_number):
    '''
    Scrapes information from the collected decks URLs and writes it into a pandas dataframe.
    Args:
        season_number   - Required  : integer number of the Hearthstone ranked season.
    Returns:
        deck_list        - Dictionary containing deck URLs as key's and names as values.
    '''
    deck_list = {}
    if season_number == 74: #For some reason, data for season 74 is under this URL
        weburl = cfg.SCRAPE_URL + str(season_number) + '-constructed-seasons'
    else:
        weburl = cfg.SCRAPE_URL + str(season_number)
    req = urllib.request.Request(weburl, headers={'User-Agent': 'Mozilla/5.0'})

    page = urllib.request.urlopen(req).read()
    soup = bs4.BeautifulSoup(page, 'html.parser')

    links = soup.find_all('h4')
    for link in links:
        deck_title = link.text.strip()
        link = link.find('a')
        deck_list[link['href']] = deck_title

    pages = soup.find('span', {'class': ['page-link', 'pages']})
    if pages is not None:
        page_text = pages.text.strip().split(' ')
        last_page = page_text[-1]
    else:
        last_page = 1

    for i in range(2, int(last_page) + 1):
        pageurl = weburl + '/page/' + str(i)
        req = urllib.request.Request(pageurl, headers={'User-Agent': 'Mozilla/5.0'})

        page = urllib.request.urlopen(req).read()
        soup = bs4.BeautifulSoup(page, 'html.parser')
        links = soup.find_all('h4')
        for link in links:
            deck_title = link.text.strip()
            link = link.find('a')
            deck_list[link['href']] = deck_title
    return deck_list


def decks_to_csv(deck_info):
    '''
    Scrapes information from the collected decks URLs and writes it into a pandas dataframe.
    Args:
        deck_info   - Required  : string containing deck name and url concatenated.
    Returns:
        data        - Pandas dataframe that contains deck's extracted infomration.
    '''
    data = pd.DataFrame(columns=cfg.DECKS_TITLE)
    req = urllib.request.Request(deck_info.split('$$$$$$$$')[0], headers={'User-Agent': 'Mozilla/5.0'})

    page = urllib.request.urlopen(req).read()
    soup = bs4.BeautifulSoup(page, 'html.parser')
    deck_code = soup.find('button', {'id': 'deck-code'})['data-deck-code']

    try:
        rating = soup.find('div', {'class': 'rating-scores'}).text.strip().replace('+', '')
    except:
        rating = 0
    try:
        date = soup.find(True, {'class': ['entry-date', 'published']}).text.strip()
    except:
        date = 'Unknown'
    try:
        uploader = soup.find(True, {'class': ['author', 'vcard']}).text.strip()
    except:
        uploader = 'Unknown'

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

    row = [deck_season, deck_info.split('$$$$$$$$')[1], deck_class, deck_code, deck_info.split('$$$$$$$$')[0], dust, rating, uploader, date, deck_format, deck_type, deck_style]
    data.loc[data.shape[0]] = row
    return data



if __name__ == '__main__':
    main()
