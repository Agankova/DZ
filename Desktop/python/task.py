import argparse
import datetime
import logging
logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', level=logging.ERROR)


def my_func(date_to_prove, value=None):
    try:
        return date_to_prove
    except KeyError:
        logging.error(f'дата недействительна')
        return value
 

parser = argparse.ArgumentParser()
parser.add_argument('date', type=lambda s: datetime.datetime.strptime(s, '%d-%m-%Y'),)
args = parser.parse_args(['08-11-2023'])
print(args.date)