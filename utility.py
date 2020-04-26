import datetime
import config as cfg


def calculate_season():
    '''
    Calculates which is the current Season in Hearthstone.
    Returns:
        season: number of the ongoing season in game.
    '''
    today = datetime.datetime.today()
    month = today.month
    year = today.year

    multiplier = year - cfg.FIRST_SEASON_YEAR

    addition = month - cfg.FIRST_SEASON_MONTH

    season = multiplier * 12 + addition + 2

    return season


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = '\r'):
    '''
    Call in a loop to create terminal progress bar
    Args:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. '\r', '\r\n') (Str)
    '''
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
