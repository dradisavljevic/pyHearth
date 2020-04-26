import requests
import config as cfg
import pandas as pd
import utility


def main():
    '''
    Module used for gathering card data from HearthstoneJSON.
    '''
    response = requests.get(cfg.CARDS_API_URL)

    data = response.json()

    dict = {}
    culled_list = {}
    exceptions = 0
    for dat in data:
        try:
            if dat['set'] not in cfg.SKIP_SETS:
                if dat['type'] in cfg.CARD_TYPES and dat['collectible'] is True:
                    if dat['type'] == 'HERO' and dat['set'] == 'CORE':
                        continue
                    if dat['set'] in dict:
                        dict[dat['set']] = dict[dat['set']]+1
                    else:
                        dict[dat['set']] = 1

                    culled_list[dat['dbfId']] = dat
        except Exception as e:
            exceptions += 1

    card_data = pd.DataFrame(columns=cfg.CARDS_TITLE)
    i = 1
    print('Saving cards to a CSV file:')
    for id, card in culled_list.items():
        utility.printProgressBar(i, len(culled_list), prefix = 'Progress:', suffix = 'Complete', length = 50)
        i += 1
        row = [id, card['name'], cfg.CARD_SETS[card['set']], card['cardClass'], card['cost'], card['rarity'], card['type'], card['id']]
        card_data.loc[card_data.shape[0]] = row

    card_data = card_data.sort_values(cfg.CARDS_SORT_COLUMN)
    card_data.to_csv(cfg.CARDS_CSV, index=False)

    print('Cards are now saved to a CSV file.')


def print_per_set(dict, culled_list):
    '''
    Analysis function. Prints out information on card types inside every set.
    '''
    for key, value in dict.items():
        neutral = 0
        priest = 0
        druid = 0
        mage = 0
        warlock = 0
        warrior = 0
        rogue = 0
        shaman = 0
        paladin = 0
        hunter = 0

        rare = 0
        common = 0
        legendary = 0
        epic = 0
        free = 0

        for dat in culled_list:
            if key == dat['set']:
                if dat['cardClass'] == 'NEUTRAL':
                    neutral += 1
                if dat['cardClass'] == 'WARLOCK':
                    warlock += 1
                if dat['cardClass'] == 'MAGE':
                    mage += 1
                if dat['cardClass'] == 'PRIEST':
                    priest += 1
                if dat['cardClass'] == 'WARRIOR':
                    warrior += 1
                if dat['cardClass'] == 'ROGUE':
                    rogue += 1
                if dat['cardClass'] == 'PALADIN':
                    paladin += 1
                if dat['cardClass'] == 'SHAMAN':
                    shaman += 1
                if dat['cardClass'] == 'DRUID':
                    druid += 1
                if dat['cardClass'] == 'HUNTER':
                    hunter += 1

                if dat['rarity'] == 'LEGENDARY':
                    legendary += 1
                if dat['rarity'] == 'RARE':
                    rare += 1
                if dat['rarity'] == 'EPIC':
                    epic += 1
                if dat['rarity'] == 'COMMON':
                    common += 1
                if dat['rarity'] == 'FREE':
                    free += 1
        print('------------------------------------------')
        print('------------------------------------------')
        print('SET ' + key + ' WITH ' + str(value) + ' CARDS:')
        print('NEUTRAL CARDS: ' + str(neutral))
        print('WARLOCK CARDS: ' + str(warlock))
        print('MAGE CARDS: ' + str(mage))
        print('PRIEST CARDS: ' + str(priest))
        print('WARRIOR CARDS: ' + str(warrior))
        print('PALADIN CARDS: ' + str(paladin))
        print('ROGUE CARDS: ' + str(rogue))
        print('HUNTER CARDS: ' + str(hunter))
        print('DRUID CARDS: ' + str(druid))
        print('SHAMAN CARDS: ' + str(shaman))
        print('------------------------------------------')
        print('COMMON CARDS: ' + str(common))
        print('RARE CARDS: ' + str(rare))
        print('EPIC CARDS: ' + str(epic))
        print('LEGENDARY CARDS: ' + str(legendary))
        print('FREE CARDS: ' + str(free))
        print('------------------------------------------')
        print('------------------------------------------')

if __name__ == '__main__':
    main()
