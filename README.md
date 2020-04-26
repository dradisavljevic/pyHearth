# pyHearth

Python scripts for acquiring deck and card data for the video game [Hearthstone](https://en.wikipedia.org/wiki/Hearthstone).

## Overview

Purpose of the project is to acquire data regarding popular Hearthstone decks by scraping the [Hearthstone Top Decks website](https://www.hearthstonetopdecks.com/) for further analysis, as well as the information on Hearthstone cards through [HearthstoneJSON API](https://hearthstonejson.com/). After scraping the decks and cards information, it is then stored inside of a .csv file for easy access.

Example of combining these two datasets is located in the decklists.txt which contains full decklist for every deck posted on Hearthstone Top Decks site for each season.


## Project structure

* scrape.py - Module used for scraping the Hearthstone Top Decks website. Uses BeautifulSoup for scraping and then stores data inside the .csv file.
* cards.py - Module used for processing JSON data acquired from HearthstoneJSON. Information on cards is then stored in another .csv file.
* textdump.py - Module that combines output of the two modules previously explained. Produces full decklist for every deck and writes it to .txt file.
* config.py - Configuration file holding all the constant values used for storing and manipulating data.
* utility.py - Module that contains helper functions i.e. for calculating number of Seasons in Hearthstone.
* [Pipfile](https://github.com/pypa/pipfile) - File used by pipenv for managing packages.
* card_list.csv - CSV file containing card information.
* deck_list.csv - CSV file containing deck information.
* decklists.txt - Text file containing decklist for every deck acquired.

## External dependencies

* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - Module used for scraping webpages.
* [Pandas](https://pandas.pydata.org/) - Library used for data manipulation as dataframe objects.
* [Requests](https://requests.readthedocs.io/en/master/) - HTTP library used to communicate with the card api.
* [Hearthstone](https://github.com/hearthsim/python-hearthstone) - Hearthstone library used for parsing deck codes.
