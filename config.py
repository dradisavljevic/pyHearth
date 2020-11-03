# Used for separating cards deemed to be important for analysis
SKIP_SETS = ['WILD_EVENT', 'CREDITS', 'HERO_SKINS', 'TAVERNS_OF_TIME', 'MISSIONS', 'BATTLEGROUNDS']
CARD_TYPES = ['MINION', 'SPELL', 'WEAPON', 'HERO']

# Hearthstone first season was on May 2014
FIRST_SEASON_MONTH = 5
FIRST_SEASON_YEAR = 2014

# URLs to Hearthstone Top Decks and HearthstoneJSON, respectively
SCRAPE_URL = 'https://www.hearthstonetopdecks.com/deck-category/constructed-seasons/season-'
CARDS_API_URL = 'https://api.hearthstonejson.com/v1/63160/enUS/cards.json'

# Column titles for .CSV files
DECKS_TITLE = ['SEASON', 'NAME', 'CLASS', 'CODE', 'URL', 'DUST', 'RATING', 'UPLOADER', 'DATE', 'FORMAT', 'TYPE', 'STYLE']
DECKS_SORT_COLUMN = 'SEASON'

CARDS_TITLE = ['DATABASE_ID', 'NAME', 'SET', 'CLASS', 'COST', 'RARITY', 'TYPE', 'INGAME_ID']
CARDS_SORT_COLUMN = 'SET'

# Translating internal representation of the Sets name
CARD_SETS = {
  'CORE': 'Basic',
  'EXPERT1': 'Classic',
  'DEMON_HUNTER_INITIATE': 'Demon Hunter Initiate',
  'DALARAN': 'Rise of Shadows',
  'ULDUM': 'Saviors of Uldum',
  'YEAR_OF_THE_DRAGON': 'Galakrond\'s Awakening',
  'DRAGONS': 'Descent of Dragons',
  'BLACK_TEMPLE': 'Ashes of Outland',
  'HOF': 'Hall of Fame',
  'NAXX': 'Curse of Naxxramas',
  'GVG': 'Goblins vs Gnomes',
  'BRM': 'Blackrock Mountain',
  'TGT': 'The Grand Tournament',
  'LOE': 'The League of Explorers',
  'OG': 'Whispers of the Old Gods',
  'KARA': 'One Night in Karazhan',
  'GANGS': 'Mean Streets of Gadgetzan',
  'UNGORO': 'Journey to Un\'Goro',
  'ICECROWN': 'Knights of the Frozen Throne',
  'LOOTAPALOOZA': 'Kobolds & Catacombs',
  'GILNEAS': 'The Witchwood',
  'BOOMSDAY': 'The Boomsday Project',
  'TROLL': 'Rastakhan\'s Rumble',
  'SCHOLOMANCE': 'Scholomance Academy',
  'DARKMOON_FAIRE': 'Darkmoon Faire'
}

# Data used to identify meta stats when scraping decks from the website
CLASS_LIST = ['Priest', 'Warlock', 'Mage', 'Warrior', 'Paladin', 'Shaman', 'Rogue', 'Hunter', 'Druid', 'Demon Hunter']
DECK_FORMATS = ['Kraken', 'Wild', 'Dragon', 'Phoenix', 'Standard', 'Mammoth', 'Raven']
DECK_TYPES = ['Aggro', 'Control', 'Midrange', 'Tempo', 'Ramp', 'Combo', 'Token', 'Fatigue', 'Mill']
DECK_STYLES = ['Tournament', 'Ladder', 'Fun', 'Theorycraft', 'Tavern-brawl']

# File names
DECKLIST_CSV = 'deck_list.csv'
CARDS_CSV = 'card_list.csv'
DECK_OUTPUT = 'decklists.txt'
