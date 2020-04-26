from hearthstone.deckstrings import Deck
import config as cfg
import pandas as pd
import os
import utility


def main():
    '''
    Module that combines data acquired on decks and cards and produces full decklists to text file.
    '''
    decks = pd.read_csv(os.path.join(os.getcwd(), cfg.DECKLIST_CSV))
    cards = pd.read_csv(os.path.join(os.getcwd(), cfg.CARDS_CSV))
    deck_dump = open(cfg.DECK_OUTPUT, 'w')

    i = 1
    print('Writing decklists to a .txt file:')
    for index, row in decks.iterrows():
        deck_code = row['CODE']
        deck = Deck.from_deckstring(deck_code)
        utility.printProgressBar(i, len(decks.index), prefix = 'Progress:', suffix = 'Complete', length = 50)
        i += 1

        deck_dump.write('Deck list for ' + row['CLASS'] + ' deck titled "' + row['NAME'] + '" from Season ' + str(row['SEASON']) + ':\n')
        for card in deck.cards:
            card_row = cards['NAME'].loc[cards['DATABASE_ID'] == card[0]]
            deck_dump.write('      ' + card_row.tolist()[0] + ' x' + str(card[1]) + '\n')
        deck_dump.write('--------------------------------------------------------------------------------------------------\n')
        deck_dump.write('--------------------------------------------------------------------------------------------------\n')


if __name__ == '__main__':
    main()
