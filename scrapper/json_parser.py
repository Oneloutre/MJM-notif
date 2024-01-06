from scrapper import scraper
from misc import webhook_handler
import re
from datetime import datetime



def extract_text(input_text):
    match = re.search(r'\[\w+\]\[\/\w+\]|[^|]+', input_text)
    if match:
        result = match.group(0)
    else:
        result = input_text
    return result


def date_transformer(input_date):
    return datetime.fromisoformat(input_date).strftime("%d/%m/%y à %H:%M")

def parser(session, webhook):
    data = scraper.recuperer_cahier_texte(session)
    for i in data:
        try:
            description, prof = scraper.analyse_page_devoirs(session, i['url'])
            webhook_handler.webhook_send(webhook, i['url'], extract_text(i['title']), i['color'], date_transformer(i['start']), i['end'], description, prof)
        except Exception as e:
            print('Erreur: ' + str(e))
            exit(1)



