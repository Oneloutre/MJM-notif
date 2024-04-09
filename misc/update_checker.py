import schedule
import time
import json
from scrapper import scraper
from misc import webhook_handler
from scrapper import json_parser
from datetime import datetime
import os


def comparer_devoirs_json(session, log_webhook):
    try:
        if not os.path.exists('files/devoirs.json'):
            with open('files/devoirs.json', 'w') as f:
                json.dump(scraper.recuperer_cahier_texte(session), f)
        with open('files/devoirs.json', 'r') as f:
            devoirs_json = json.load(f)
        devoirs = scraper.recuperer_cahier_texte(session)
        if devoirs == devoirs_json:
            print('Pas de nouveaux devoirs | ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            webhook_handler.simple_send(log_webhook, 'Pas de nouveaux devoirs | ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            diff_elements = [item for item in devoirs if item not in devoirs_json]
            for i in diff_elements:
                webhook = webhook_handler.webhook_check()
                description, prof = scraper.analyse_page_devoirs(session, i['url'])
                webhook_handler.webhook_send(webhook, i['url'], json_parser.extract_text(i['title']), i['color'], json_parser.date_transformer(i['start']), json_parser.date_transformer(i['end']), description, prof)
            with open('files/devoirs.json', 'w') as f:
                json.dump(devoirs, f)
    except Exception as e:
        print('Erreur: ' + str(e))
        exit(1)
